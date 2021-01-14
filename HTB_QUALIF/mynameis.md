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
