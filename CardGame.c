#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>

int random_number(up_to);

//Struct com as iformações de cada personagem
typedef struct 
{   
    char nome[50];
    int hp;
    int damage;

} Personagens_jogaveis;




void
main()
{
    //Declaração dos personagens
    Personagens_jogaveis personagem[4];
    
    //Definição da vida e dano de cada um:

    //Mago
    strcpy(personagem[0].nome, "Mago");
    personagem[0].hp = 10;
    personagem[0].damage = 15;

    //Bárbaro
    strcpy(personagem[1].nome, "Barbaro");
    personagem[1].hp = 20;
    personagem[1].damage = 10;

    //Assassino
    strcpy(personagem[2].nome, "Assassino");
    personagem[2].hp = 5;
    personagem[2].damage = 25;

    //Goblin
    strcpy(personagem[3].nome, "Goblin");
    personagem[3].hp = 10;
    personagem[3].damage = 5;


    //Declaração de variáveis para o código
    int 
        num = 4; //quantidades de cartas no jogo
    int 
        random = 0,         //Salva números aleatórios
        old_random = -1,    //Evita que os números aleatórios sejam iguais        
        contador = 0;       //Auxilia o array que guarda quais herois foram dados para o usuário e adversário
          

    int 
        index = 0,          //Verifica qual heroi foi escolhido pelo usuário para jogar
        numero_heroi = 0;  

    char
        herois_usu[2],      //Array para salvar os índices dos heróis dados para cada jogador 
        herois_adv[2];      //(O tamanho do Array depende da quantidade de cartas que cada jogador terá)


    //Auxiliar para que os números sejam fielmente aleatórios
    srand(time(NULL));

    //Indicando as cartas do adversário (PC) para fins de testes
    printf("==============================\n");
    printf("O Computador tem as cartas: \n");
    for (int count = 0; count < 2; count++)
    {
        //Guardar um número aleatório de um Herói
        random = rand() % num;

        //Evitar que a carta seja igual a anterior e entregue apenas cartas iguais para os jogadores
        while (random == old_random)
        {
            random = rand() % num;
        }
        old_random = random;

        //Printar na tela os atributos de cada personagem
        printf("Heroi %d:\n", count + 1);
        printf("%s\n", personagem[random].nome);
        printf("Com vida de: %d\n", personagem[random].hp);
        printf("Com dano de: %d\n", personagem[random].damage);

        //Salvando os índices (na struct) dos heróis (dados)
        herois_adv[contador] = random;
        contador++;

        printf("==============================\n");
    }


    //Indicando as cartas do jogador (2 cartas para cada um)
    contador = 0;

    printf("O Usuario tem as cartas: \n");
    for (int count = 0; count < 2; count++)
    {
        //Guardar um número aleatório de um Herói
        random = rand() % num;

        //Evitar que a carta seja igual a anterior e entregue apenas cartas iguais para os jogadores
        while (random == old_random)
        {
            random = rand() % num;
        }
        old_random = random;

        //Printar na tela os atributos de cada personagem
        printf("Heroi %d:\n", count + 1);
        printf("%s\n", personagem[random].nome);
        printf("Com vida de: %d\n", personagem[random].hp);
        printf("Com dano de: %d\n", personagem[random].damage);

        //Salvando os índices (na struct) dos heróis (dados)
        herois_usu[contador] = random;
        contador++;

        printf("==============================\n");
    }

    //Item para testes
    // for (int count = 0; count < 2; count++)
    //     printf("%d\n", herois_usu[count]);
    

    
    //Perguntando ao usuário qual carta ele irá querer 
    printf("Jogador, escolha a sua carta para jogar:(1)/(2) ");
    scanf("%d", &index);

    //O usuário digitará 1 ou 2 para o herói, mas ele se encontra na posição 0 ou 1 no array, então tira 1 do index
    numero_heroi = herois_usu[index - 1];

    //Printando na tela o herói escolhido pelo usuário
    printf("O Herois escolhido foi: \n");
    printf("%s\n", personagem[numero_heroi].nome);
    printf("Com vida de: %d\n", personagem[numero_heroi].hp);
    printf("Com dano de: %d\n", personagem[numero_heroi].damage);


    

    printf("=============================\n");
    printf("O Herois escolhido pelo PC foi: \n");
    printf("%s\n", personagem[random].nome);
    printf("Com vida de: %d\n", personagem[numero_heroi].hp);
    printf("Com dano de: %d\n", personagem[numero_heroi].damage);


    //Pegar os heróis do pc 
    //fazer o heroi do pc ser pego aleatoriamente 
    //fazer rounds tirando vida com o dano 
    //Pensar em como adicionar efeitos
}
