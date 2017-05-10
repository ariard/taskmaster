#include <signal.h>
#include <stdio.h>
#include <stdlib.h>

static void handler(int signum)
{
	printf("Kill by %d", signum);
	printf("Do nothing");
}

int		main(void)
{	
	struct sigaction sa;

	sa.sa_handler = handler;
	sigemptyset(&sa.sa_mask);
	sa.sa_flags = SA_RESTART;

	if (sigaction(SIGINT, &sa, NULL) == -1)
	{
		printf("Error sigaction");
		exit(0);
	}
	if (sigaction(SIGTERM, &sa, NULL) == -1)
	{
		printf("Error sigaction");
		exit(0);
	}
	if (sigaction(SIGHUP, &sa, NULL) == -1)
	{
		printf("Error sigaction");
		exit(0);
	}
	if (sigaction(SIGUSR1, &sa, NULL) == -1)
	{
		printf("Error sigaction");
		exit(0);
	}
	printf("Sigaction good");
	while (1);
	return (0);
}	
