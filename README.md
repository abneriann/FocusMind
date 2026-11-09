# FocusMind

> **Evolua do seu jeito.**

O **FocusMind** é uma plataforma de evolução pessoal criada para reunir estudos, produtividade, atividade física, gamificação e comunidade em uma experiência integrada. O projeto busca ajudar cada pessoa a organizar sua rotina, acompanhar o próprio progresso e construir constância respeitando seus objetivos e seu ritmo.

## Desenvolvedores

- **Abner Alencar**
- **Marcelo Sanches**

## Problema

Quem deseja evoluir em diferentes áreas da vida costuma depender de várias ferramentas isoladas: uma para estudos, outra para treinos, outra para hábitos e outras para comunicação ou acompanhamento de metas. Essa fragmentação dificulta a organização da rotina, reduz a visão do progresso e pode prejudicar a motivação ao longo do tempo.

O FocusMind propõe centralizar essas experiências, tornando o desenvolvimento pessoal mais claro, estimulante e conectado.

## Público-alvo

O projeto é voltado para estudantes, profissionais e demais pessoas interessadas em:

- organizar estudos e sessões de foco;
- desenvolver hábitos mais saudáveis;
- acompanhar metas e evolução pessoal;
- participar de equipes e desafios coletivos;
- manter a motivação por meio de missões e conquistas.

## Como funciona

A visão do FocusMind é permitir que o usuário defina seus focos, registre atividades e acompanhe sua evolução em quatro módulos complementares:

| Módulo | Objetivo |
| --- | --- |
| **FocusLearn** | Estudos, produtividade e monitoramento de sessões. |
| **FocusMove** | Atividade física, treinos e hábitos saudáveis. |
| **FocusLevel** | XP, níveis, missões e conquistas. |
| **FocusTeams** | Equipes, comunidades, desafios coletivos e comunicação. |

Esta primeira etapa apresenta apenas a proposta do produto em uma página institucional estática. As funcionalidades descritas representam a visão de longo prazo e serão implementadas gradualmente.

## Tecnologias planejadas

### Interfaces

- **Web:** React + TypeScript;
- **Mobile:** React Native para Android e iOS;
- **Desktop:** Electron + React.

### Backend e dados

- **API:** ASP.NET Core com C#;
- **Banco de dados:** PostgreSQL;
- **Autenticação:** Supabase Auth;
- **Comunicação em tempo real:** SignalR;
- **Voz (etapa futura):** WebRTC.

### Primeira entrega

- HTML5 semântico;
- CSS3 responsivo;
- Git e GitHub para versionamento.

## Estrutura atual

```text
FocusMind/
├── .gitignore   # Arquivos e diretórios ignorados pelo Git
├── index.html   # Página inicial responsiva do projeto
└── README.md    # Documentação e visão geral
```

A estrutura inicial é propositalmente pequena para atender à atividade acadêmica sem antecipar a implementação completa do sistema. Na evolução do produto, os clientes web, mobile e desktop e o backend poderão ser organizados em diretórios próprios.

## Arquitetura planejada

O FocusMind será um ecossistema multiplataforma. A página `index.html` desta entrega é apenas a apresentação institucional inicial, não o aplicativo completo. A evolução prevista separa cada cliente e o backend, permitindo que todos compartilhem as mesmas regras de negócio e dados por meio da API.

```text
FocusMind/
├── apps/
│   ├── web/          # Site e aplicação web em React + TypeScript
│   ├── mobile/       # Aplicativo Android e iOS em React Native
│   └── desktop/      # Aplicativo desktop em Electron + React
├── services/
│   └── api/          # Backend em ASP.NET Core / C#
├── docs/             # Documentação técnica e de produto
└── README.md
```

Essa estrutura é uma referência para as próximas etapas e ainda não foi criada, evitando adicionar código ou dependências fora do escopo da atividade atual.

## Como executar

Esta versão não exige instalação de dependências.

1. Clone o repositório:

   ```bash
   git clone <URL-DO-REPOSITORIO>
   ```

2. Entre no diretório do projeto:

   ```bash
   cd FocusMind
   ```

3. Abra o arquivo `index.html` diretamente no navegador.

Como alternativa, utilize um servidor HTTP local. Com Python instalado:

```bash
python -m http.server 8000
```

Depois, acesse `http://localhost:8000`.

## Identidade visual

A interface respeita a identidade visual aprovada do FocusMind:

- preto;
- branco;
- laranja `#FF702B`.

Nenhuma nova logo foi criada nesta etapa. Quando os arquivos oficiais estiverem disponíveis, eles poderão ser incorporados sem alterar a estrutura da página.

## Melhorias futuras

- migrar a interface web para React + TypeScript;
- criar autenticação e perfis de usuário;
- implementar sessões de estudo e produtividade no FocusLearn;
- adicionar treinos, hábitos e indicadores no FocusMove;
- desenvolver o sistema de XP, níveis, missões e conquistas do FocusLevel;
- criar equipes, comunidades, desafios e mensagens no FocusTeams;
- implementar a API em ASP.NET Core e persistência em PostgreSQL;
- integrar Supabase Auth e SignalR;
- desenvolver aplicativos mobile e desktop;
- avaliar chamadas de voz por WebRTC;
- ampliar testes, acessibilidade, segurança e observabilidade.

## Status do projeto

🚧 **Em desenvolvimento — etapa inicial acadêmica.**

O foco atual é estabelecer a documentação, o versionamento e uma apresentação responsiva do conceito. O sistema completo ainda não está implementado.

## Licença

Ainda não foi definida uma licença para o projeto.
