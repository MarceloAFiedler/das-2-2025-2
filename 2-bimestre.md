# AULA 08/10/2025

## RBAC X ABAC

- Role Based Access Control -> dar permissão de acordo com o papel (role)
- criar groups
- documento -> policys
- grupos só podem ter pessoas dentro
- usa IAM da amazon

## ABAC

- Attribute Based Access Control
- a permissao so vale se o recurso da nuvem que estiver sendo utilizado tiver um atributo especial
- tagging aws tem que ter chave, valor (owner, nome das pessoas)
- a policy só é valida se tiver uma tag de permissionamento

## USUARIOS FEDERADOS

- logar com conta de outro sistema (logar com google, microsoft, github, etc)
- protocolos: openID e SAML
- pra ajudar com isso -> identity center aws

## STS 

- especie de usuario federado
- token temporario para permissoes

## AMAZON COGNITO

- autenticacao e autorizacao e gerenciamento de users para web e mobile
- identity provider b2c
- integra com "logins federados"
- user pool

## AWS Organization

- escolhe uma ponta para ser a "PÁI"
- tem que aceitar pra ser "filha"
- OU (organizations units) para separar "equipes"
- governança -> ser pego fazendo algo fora do padrão eu "perco" (SCPs)

## CRIPTOGRAFIA

- esconder uma informação valiosa pelo tempo necessário, enquanto a informação ainda é relevante
- criptografia simetrica = chaves que criptografa e descriptografa é a mesma (uma chave faz os dois trabalhos)
- criptografia assimetrica = duas chaves, chave publica e privada (uma criptografa outra descriptografa)

## WAF 

- Web Application Firewall
- pra evitar sql injection

## MACIE

- varre o S3 e DB para encontrar PII

## INSPECTOR

- analisa codigo e verifica se tem vulnerabilidade em open sources

## DETECTIVE

- ajuda a investigar a causa raiz em coisas estranhas na conta
- analisar como aconteceu o problema


# AULA 22/10/2025

## route 53 (enderecos de dns)

- dificilmente cai (raro, tirando segunda dia 20/10/2025)
- resolve dns publico (na net) e privado (dentro da rede)

### Policies
  - Geolocalização -> Devolve um IP daquele país
  - Latência -> Resolve o servidor mais próximo
  - Peso -> 50% das req para X lugar, etc
  - Failover -> To mandando para north-vir, north-vir caiu, manda pro Brasil
  - Simples -> 1:1 (nome:IP)
  - Multivalue -> retorna uma lista de IP e o cliente decide
  - IP Based -> ip do lucaspacifico

### dominios para saber
- A -> ipv4
- AAAA -> ipv6
- cname -> um dns aponta pra outro
- txt -> informacao qualquer que coloca no dns para provar que é seu mesmo

## modulo 11: Automating Your Architecture

- parar de fazer as coisas na mão, automatizar

### IaC (infraestrutura como codigo)

- definir um arquivo(template) descrevendo como tu precisa, e uma ferramenta faz pra voce
- CloudFormation, ferramenta de iac da aws

- beneficios:
  - escreve um template e ele gera (pode guardar no git)
  - reusabilidade
  - cria stack

### IaC services que usam CloudFormation
- aws elastic beanstalk ***aprender
- aws quick starts
- aws seversless application model (SAM) ***aprender
- aws amplify
- aws cloud development kit

### Amazon Q developer
- IA generativa da aws
- para devs e profissionais de ti


# AULA 29/10/2025

## CACHING

- pra redução de latencia

### por que cache?

- nao da pra toda vez bater no banco fazer a mesma query e voltar
- dados que são acessados frequentes
- dados muito pesados pra carregar
- pra quando tem consultas lentas e caras
- dados que são estáticos

### trade-offs

pros
- performance previsivel
- reduzir custo
- reduz latencia

contras
- mudar a lógica
- gerenciar o cache, manter no ar

### TIPOS DE CACHING

- cache em memoria
- cache na aplicação inteira

### CACHE CLOUDFRONT

- CDN
  - rede global de servidores pra entregar conteudos comuns

- cache de imagem
- cache de html, css e javascript

- edge location
  - perto do user
  - cache menor
    
- regional edge location
  - mais distante do usuario
  - cache maior
 
### Elastic Cache

- quando tem problema de tempo de resposta
- quando nao da mais tempo de responder
- reduzir custo

- pergunta pra ele (elasticache) primeiro, depois pro banco

- MenCache
  - basico
  - rodar grandes nós com multiplos nucleos ou threads
  - escala horizontal
 
- Redis
  - usa o disco
  - suporta tipos de dados complexos
  - pub/sub
  - mapeamento

- elasticache pode chegar ate 250 maquinas (o cluster)

- TTL (time to live)
  - segundos ate a key "patchon"






