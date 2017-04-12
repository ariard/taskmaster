#include <unistd.h>
#include <fcntl.h>

int 	main(void)
{
	int		fd;

	fd = open("/tmp/others", O_CREAT | O_WRONLY, 0644);
	while (1)
	{
		write(fd, "server\n", 7);
		sleep(5);
	}
	return (0);
}
