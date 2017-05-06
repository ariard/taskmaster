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
	int		file;
	int		out;

	fd = open("/dev/stdin", O_RDONLY);
	file = open("/tmp/file", O_CREAT | O_WRONLY | O_APPEND, 0644);
	while (1)
	{
		bzero(buf, 128);
		read(fd, buf, 128);
		garb = strchr(buf, '\n');
		*garb = 0;
		write(file, buf, 128);
		write(STDOUT_FILENO, "your data [", 11);
		write(STDOUT_FILENO , buf, 128);
		write(STDOUT_FILENO, "]\n", 2);
	}
	return (0);
}
