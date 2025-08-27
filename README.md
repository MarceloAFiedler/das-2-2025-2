# das-2-2025-2
Conteúdo da disciplina de Design e Arquitetura de Software 2

# Aula 30/07/2025

## CURSO AWS

### Objetivos:
  - boas práticas
  - serviços da AWS
  - Well-architected framework (https://aws.amazon.com/pt/architecture/well-architected/)

-  cenário ficticio de uma cafeteria que quer passar a utilizar aws, um ecommerce

### etapas do arquiteto
  - planejamento (plan)
  - pesquisa (research)
  - construção (build)

### Architected Framework
  - operational excellence: melhorar, deixar continuo, ver como código, automatizar tudo que puder
  - security: criar mecanismos de identidade seguro, segurança em todas camadas, rastreabilidade, mitigação de estratégias
  - reliabillity: recuperação rápida, mitigar desrupção, dinâmico demanda de computador
  - performance efficiency: manter recursos eficientes, escalar de forma automatica, democratizar uso de tecnologias novas
  - cost optimization: medir eficiência, eliminar oq não está sendo utilizado, modelo por consumo, serviço gerenciado 
  - sustainabillity: utilizar recursos de forma sustentável

### Well architected tool
- testar se o sistema está "well"

### Trade-offs
- escolhas
- abrir mão de consistencia para ter performance, ex: tiktok, reels
- escalabilidade por custo (cloudwatch, "vigia" se esta aumentando consumo e tudo mais)

### Design de serviços, não de servidores
- fila
- site estático
- autenticação

### Escolher tamanho errado
- storage errado
- latencia
- concorrencia

### evitar ponto singulares de falhas
- database secundário como cópia e assumir caso caia

### otimização de custo
- tem que medir e monitorar
- o que devo monitorar?
- desativar recursos que não uso
- serviços gerenciados!


# AULA 06/08/2025

## REGIOES E DATA CENTERS

### AZ
- Dentro de regioes disponiveis da aws tem zonas, onde podemos subir servidores
- AZ estrutura logica da AWS, um conjunto de datacenters e é composto por um ou mais datacenters
- AZs são interconectadas
- pode escolher a rede que voce quer usar
- ALTA DISPONIBILIDADE!

### LOCAL ZONE
- ip local que esta em uma zona diferente

### DATA CENTERS
- ninguem tem acesso aos data centers da AWS

### AWS PoPs
- edge location = data centers e servers próximos dos clientes
- regional edge cache = ponte entre origin server e edge location


## SECURING ACCESS

### INTRODUCING
- modelo de responsabilidade da AWS, sempre compartilhada
- IaaS, PaaS, SaaS

### DESIGN PRINCIPLES FOR THE SECURITY PILLAR
- cuidar das credenciais
- protecao de dados em transito e estatico
- DEIXAR PESSOAS LONGES DE DADOS
- seguranca em todas as camadas
- manter traceabilidade
- preparar treinamentos de seguranca
- automatizar processos de seguranca

### PRINCIPIO DE PRIVILEGIO MINIMO
- nao de adm pra todo mundo

### USAR CRIPTOGRAFIA EM TODO LUGAR!

### AUTHENTICATING AND SECURING ACCESS
- AUTENTICACAO = saber se voce é voce mesmo, quem voce é, o que voce sabe, o que voce tem
- AUORIZACAO = dizer o que voce pode fazer

### AWS IAM
- criar users, group, role e policy
- integrar AWS services
- MFA multi factor aunthentication
- permissao em nivel de arquivo

### BOAS PRATICAS
- privilegio minimo
- MFA
- rotacao de credeniais
- senhas fortes
- credenciais locais protegidas
- aws organization
- aws cloudtrail!!!
- proteger usuario raiz

### ROLE
- credencial temporaria


# AULA 20/08/2025

## MODULO 4

### STORAGE
- block storage, armazenado em blocos de tamanho fixados
- file storage, pastas compartilhadas
- object storage, subir objetos na internet, baseado em atributos e metadados (metados = dados sobre dados)

### AMAZON S3
- virtualmente ilimitado
- armazena em "buckets" que voce define
- 5 tera de limite por objeto
- ganha URL unica (n exposta pra net)
- nome do bucket faz parte da URL
- nao existe pasta, as "pastas" sao prefixos

- usado para hospedar sites estaticos
- suporta qualquer pico de demanda
- utilizado para recuperacao de desastres

### CORS
- validacao que acontece no navegador
- "negocio que enche o saco"
- relacao de confianca entre o back e front


  # AULA 27/08/2025

  ### INVENTARIO S3
  - gera relatorio dos objetos do bucket
  - 
