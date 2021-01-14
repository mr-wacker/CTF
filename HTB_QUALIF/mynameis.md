# Intro

Executing a file returns the following result

```bash
> ./my_name_is
Who are you?
No you are not the right person
```

Anaylyse what kind of file "file"

```bash
> file my_name_is
my_name_is: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=c8d536794885d0c91e2270d7c6b9a9f14dda9739, not stripped
```

Get strings of a text file and parse the line that's longer than 8 letters

```bash
strings -o my_name_is
grep -Po ".{8,} ./my_name_is
```

Ghidra analysis

```c
void main(void)

{
  EVP_PKEY_CTX *ctx;
  __uid_t __uid;
  passwd *ppVar1;
  long lVar2;
  int iVar3;
  size_t sVar4;
  size_t *outlen;
  uchar *in;
  size_t in_stack_ffffffd0;
  int local_28;
  
  puts("Who are you?");
  __uid = geteuid();
  ppVar1 = getpwuid(__uid);
  in = (uchar *)0x0;
  lVar2 = ptrace(PTRACE_TRACEME,0,0);
  if (lVar2 != 0) {
    puts("This doesn\'t seem right");
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  if (ppVar1 != (passwd *)0x0) {
    ctx = (EVP_PKEY_CTX *)ppVar1->pw_name;
    iVar3 = strcmp((char *)ctx,username);
    if (iVar3 == 0) {
      local_28 = 0;
      while (local_28 < 0x198) {
        if ((*(uint *)(main + local_28) & 0xff) == breakpointvalue) {
          puts("What\'s this now?");
                    /* WARNING: Subroutine does not return */
          exit(1);
        }
        local_28 = local_28 + 1;
      }
      sVar4 = strlen(encrypted_flag);
      outlen = (size_t *)malloc((sVar4 + 1) * 4);
      decrypt(ctx,encrypted_flag,outlen,in,in_stack_ffffffd0);
      *(undefined *)((int)outlen + sVar4) = 0;
      puts((char *)outlen);
    }
    else {
      puts("No you are not the right person");
    }
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  puts("?");
                    /* WARNING: Subroutine does not return */
  exit(1);
}
```

The flow of program 
1.   puts("Who are you?");
  __uid = geteuid();
  ppVar1 = getpwuid(__uid);

The initial gateway to check the user_id.

2.     if iVar3 = strcmp((char *)ctx,username){
        ... decrypt(ctx,encrypted_flag,outlen,in,in_stack_ffffffd0);

Comparing ctx(userinput) with username variable "7e 23 4c 2d 3a 34 3b 66" = ~#L-:4;f

Basically, if the current executing username matches it, it will decrypt the stored flag and output.

However, 
This username contains illegal characters that we can't make such user on the system.

Linux system checks the dynamic linker and its eniviromental variable `LD_PRELOAD` for libraries.
If over-ridden, the library will be linked. Using this method, we can overwrite  `ppVar1 = getpwuid(__uid);` part

This is the contents of `pwd.h`

```c
    #include <pwd.h>
    struct passwd *getpwuid(uid_t);
 DESCRIPTION
    The <pwd.h> header provides a definition for struct passwd, which includes at least the following members:

    char    *pw_name   user's login name
    uid_t    pw_uid    numerical user ID
    gid_t    pw_gid    numerical group ID
    char    *pw_dir    initial working directory
    char    *pw_shell  program to use as shell
```

So We'll make a preloaded library that will create pw_name to be `~#L-:4;f`.
pw_passwd can be anything. `pw_uid` and `pw_gid` is set to `0` means `root` (not necessary)

```c
#include <sys/types.h>
#include <stdlib.h>
#include <pwd.h>

long ptrace(int request, pid_t pid,
                   void *addr, void *data) {
	return 0;
}

struct passwd *getpwuid(uid_t uid) {
	struct passwd* ret = malloc(sizeof(struct passwd));
	ret->pw_name = "~#L-:4;f";
	ret->pw_passwd = "a";
	ret->pw_uid = 0;
	ret->pw_gid = 0;
	return ret;
}
```

On bash terminal, the followings are executed

```bash
/home/kali/Desktop [kali@kali] [5:16]
> gcc -m32 main.c -shared -o preload.so

/home/kali/Desktop [kali@kali] [5:17]
> file preload.so
preload.so: ELF 32-bit LSB shared object, Intel 80386, version 1 (SYSV), dynamically linked, BuildID[sha1]=f85930e222e291b6723214cab29c9ca567f8e0fd, not stripped

/home/kali/Desktop [kali@kali] [5:17]
> LD_PRELOAD=/home/kali/Desktop/preload.so ./my_name_is
Who are you?
HTB{L00k1ng_f0r_4_w31rd_n4m3}
```

So, you'd basically create preloadable library that'll be linked to an executable of `my_name_is`

