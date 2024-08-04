#include <stdio.h>
#include <string.h>
int main(int argc, char *argv[]) {
char buf[1024];
int admin = 0;
char command[1024];
strcpy(buf, argv[1]);
strcpy(command, argv[2]);
printf("admin %d\n", admin);
if (admin != 0) {
   setuid(0);
   system(command);

}else{
   system(command);
}


return 0;
}

