#include <stdio.h>
#include <client_version.h>
#include <server_version.h>


int main(int argc, char ** argv) {
    printf("client version: %s\n", getClientVersion());
    printf("server version: %s\n", getServerVersion());
    return 0;
}
