#include<stdio.h>
#include<string.h>

int buscarUsuario(char *nombre){
	char *nombres[50] = {"user1", "user2", "user3", 
		"user4", "user5","adminA", "adminB", "adminC"};
	
	for(int i = 0; i < 8; i++){
		if(strcmp(nombres[i], nombre) == 0){
			return i;
		}
	}
	return -1;
}

int leerUsuario(){
	char nombre[50];
	printf("Escribe tu nombre:\n");
	scanf("%s", nombre);
	int idUsuario = buscarUsuario(nombre);
	if(idUsuario != -1){
		return idUsuario;
	}
	return -1;
}

char *descifrar(char *password){
	int longitud = strlen(password);
	for(int i = 0; i < longitud; i++){
		password[i] = password[i] - 3;
	}
	return password;
}

int buscarPassword(char *password, int idUsuario){
	char passwords[8][50] = {"sdvv4", "sdvv5", "sdvv6", "sdvv7", "sdvv8",
							 "dgplq4", "dgplq5", "dgplq6"};
	
	for(int i = 0; i < 8; i++){
		descifrar(passwords[i]);
	}

	for(int i = 0; i < 8; i++){
		if(strcmp(passwords[i], password) == 0 && i == idUsuario){
			return 1;
		}
	}
	return 0;
}

int leerPassword(int idUsuario){
	char password[50];
	printf("Escribe tu password:\n");
	scanf("%s", password);
	return buscarPassword(password, idUsuario);
}

int main(){
	int idUsuario = leerUsuario();
	if(idUsuario == -1){
		printf("Usuario no encontrado\n");
		return 0;
	}

	int password = leerPassword(idUsuario);
	if(password == 0){
		printf("Password incorrecto\n");
		return 0;
	}
	
	printf("Bienvenido\n");
	return 0;
}
