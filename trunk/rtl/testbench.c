#include "stdio.h"
#include <stdio.h>
char str[] = "Hallo, Welt!\r\n";
/*char str[] = "1";*/
int main()
{
    volatile char *led = (char *) 0xffffffb0;
    *led = (char) 0xaa;
    xil_printf(
                /*"02"*/
	    "0:Hello, world!\r\n"
	    "1:Hello, world!\r\n"
	    "2:Hello, world!\r\n"
	    "3:Hello, world!\r\n"
	    "4:Hello, world!\r\n"
	    "5:Hello, world!\r\n"
	    "6:Hello, world!\r\n"
	    "7:Hello, world!\r\n"
	    "8:Hello, world!\r\n"
	    "9:Hello, world!\r\n"
	    "a:Hello, world!\r\n"
	    "b:Hello, world!\r\n"
	    "c:Hello, world!\r\n"
	    "d:Hello, world!\r\n"
	    "e:Hello, world!\r\n"
	    "f:Hello, world!\r\n"
    );
    xil_printf(str);
    *led = (char) 0xff;
    return 0;
}
