#include <stdio.h>
#include <unistd.h>
#include <strings.h>
#include <fcntl.h>
#include <string.h>

int		main(void)
{
	char	buf[128];
	char	*garb;
	int		fd;
	int		out;
	int		debug;

	debug = open("/tmp/special_debug", O_CREAT | O_WRONLY | O_APPEND, 0644);
	write(debug, "\n\n", 4);
	write(debug, "after debug init\n", strlen("after debug init\n"));
	fd = open("/dev/stdin", O_RDONLY);
	write(debug, "loop read\n", strlen("loop read\n"));
	while (1)
	{
		bzero(buf, 128);
		write(debug, "before read\n", strlen("before read\n"));
		read(fd, buf, 128);
		write(debug, "after read, buf is\n", strlen("after read, buf is\n"));
		write(debug, buf, strlen(buf));
		garb = strchr(buf, '\n');
		write(debug, "elim garb\n", strlen("elim garb\n"));
		if (garb && *garb)
			*garb = 0;
		write(debug, "after garb\n", strlen("after garb\n"));
		write(debug, "wrting\n", strlen("wrting\n"));
		write(STDOUT_FILENO, "your data [", 11);
		write(STDOUT_FILENO , buf, 128);
		write(STDOUT_FILENO, "]\n", 3);
		write(debug, "after written\n", strlen("after written\n"));
	}
	return (0);
}
