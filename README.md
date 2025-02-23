# ponderada-prog_m9s3

&emsp; Esse repositório é respectivo a entrega da ponderada da semana 3, sendo ela:

Selecione uma empresa digital e descreva como algum aspecto não funcional da sua arquitetura é sustentada por códigos que suportam a operação:
1) Documentar os requisitos em código (1 RF - 5.0 pontos); 
2) Aferir a qualidade dos requisitos envolvidos no sistema, ao executar estes códigos (1 RNF - 5.0 pontos).

&emsp;A empresa escolhida foi a Netflix, que é uma das maiores plataformas de streaming do mundo e precisa garantir a disponibilidade e escalabilidade do seu sistema, mesmo sob alta demanda. Um aspecto não funcional fundamental para sua operação é a Resiliência, que impede que falhas de servidores ou sobrecargas afetem a experiência do usuário.

1) Documentação do Requisito Funcional (RF) em Código
Requisito Funcional (RF):
A plataforma deve permitir que usuários assistam a conteúdos sob demanda sem interrupções, mesmo quando houver falhas em servidores específicos.
Para isso, um sistema de fallback deve redirecionar requisições para servidores alternativos caso um servidor fique indisponível.

Código que Documenta o RF: <link>
