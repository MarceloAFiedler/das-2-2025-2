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











  
