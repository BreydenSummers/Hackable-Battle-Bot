#include <stdio.h>
#include <string.h>
int main(int argc, char *argv[]) {
// Buffer size is obscured for security reasons
char buf[¯\_(ツ)_/¯];
int admin = 0;
// Buffer size is obscured for security reasons
char command[¯\_(ツ)_/¯];
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

