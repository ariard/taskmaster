#include <signal.h>
#include <unistd.h>

int main(void)
{
	int status;

	status = getpid();
	kill(status, 11);
	return (0);
}
