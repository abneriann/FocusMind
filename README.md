# FocusMind

> **Evolua do seu jeito.**

**FocusMind** é uma plataforma de evolução pessoal que une aprendizagem, atividade física, hábitos, gamificação e comunidade em uma experiência acessível, moderna e motivadora.

Nosso objetivo é ajudar pessoas de diferentes idades a desenvolver seu potencial, respeitando seus ritmos, dificuldades e conquistas.

**Status:** Em planejamento e desenvolvimento inicial. As funcionalidades descritas são objetivos do projeto e ainda não estão disponíveis para uso.

## Entrega acadêmica atual

Esta primeira entrega de versionamento mantém o escopo propositalmente pequeno e contém:

```text
FocusMind/
├── assets/icons/             # Pack oficial de ícones em SVG e PNG
├── scripts/                  # Geração dos PNGs a partir dos SVGs
├── .gitignore                # Regras de arquivos ignorados pelo Git
├── index.html                # Apresentação institucional responsiva
└── README.md                 # Documentação do projeto
```

A página atual apresenta o conceito e os quatro módulos sem antecipar a implementação completa do produto. A evolução planejada separará as aplicações web, mobile e desktop e a API em diretórios próprios dentro do monorepo.

### Como executar a página

Não é necessário instalar dependências. Clone o repositório e abra `index.html` no navegador. Opcionalmente, execute um servidor local:

```bash
python -m http.server 8000
```

Depois, acesse `http://localhost:8000`.

## Nossa missão

Transformar a maneira como as pessoas estudam, cuidam do corpo e acompanham seu desenvolvimento pessoal.

Acreditamos que evoluir não significa ser perfeito todos os dias, mas encontrar ferramentas e oportunidades para continuar crescendo.

O FocusMind não é uma ferramenta de diagnóstico ou tratamento de condições de saúde.

## O ecossistema FocusMind

### FocusLearn — Aprenda do seu jeito

Um ambiente inteligente para tornar os estudos mais organizados e produtivos.

**Funcionalidades planejadas:**
- Cronômetro de estudos manual e inteligente opcional.
- Registro de sessões, pausas e tempo efetivo de concentração.
- Organização de matérias, objetivos e conteúdos.
- Histórico e relatórios de produtividade.
- Recomendações de aulas, vídeos e professores.
- Trilhas de aprendizagem personalizadas.
- Avaliações e recomendações feitas pela comunidade.

### FocusMove — Movimento é evolução

Um espaço dedicado à atividade física, ao bem-estar e à construção de hábitos saudáveis.

**Funcionalidades planejadas:**
- Registro de treinos e exercícios.
- Caminhadas e corridas.
- Desafios físicos individuais e coletivos.
- Acompanhamento de hidratação.
- Metas adaptáveis a diferentes níveis.
- Histórico de atividades e evolução.
- Incentivo ao descanso e à recuperação.

### FocusLevel — Cada conquista importa

Sistema de gamificação que reconhece a evolução do usuário.

**Funcionalidades planejadas:**
- Pontos de experiência (XP).
- Níveis e conquistas.
- Missões pessoais.
- Temporadas e desafios especiais.
- Rankings equilibrados.
- Recompensas virtuais.
- Progresso integrado entre os módulos.

A gamificação deve incentivar a consistência sem punir o usuário por pausas ou dias difíceis.

### FocusTeams — Evoluir juntos

Um ambiente social para compartilhar conhecimento, experiências e conquistas.

**Funcionalidades planejadas:**
- Criação e personalização de equipes.
- Convites, membros e funções.
- Feed de estudos, treinos e conquistas.
- Publicações com imagens.
- Chat de texto.
- Salas de voz.
- Sessões coletivas.
- Desafios entre equipes.
- Rankings coletivos.
- Privacidade, denúncias e moderação.

## Plataformas

O FocusMind foi planejado para oferecer uma experiência integrada em:

- **Web:** navegadores modernos.
- **Android:** aplicativo mobile.
- **iOS:** aplicativo mobile.
- **Windows:** aplicativo desktop.
- **macOS:** possibilidade de expansão futura.

A proposta é que todas as plataformas compartilhem a mesma conta e sincronizem os dados de evolução.

## Tecnologias planejadas

| Camada | Tecnologia |
|---|---|
| Frontend Web | React + TypeScript |
| Aplicativo Mobile | React Native |
| Desktop | Electron + React |
| Backend | C# / ASP.NET Core |
| Banco de dados | PostgreSQL |
| Autenticação | Supabase Auth |
| Armazenamento | Storage |
| Comunicação em tempo real | SignalR |
| Chamadas de voz | WebRTC |
| Análises inteligentes futuras | Python |

A arquitetura será organizada em um monorepo, facilitando o compartilhamento de componentes, tipos, regras e funcionalidades.

As escolhas tecnológicas poderão ser validadas durante a implementação.

## Identidade visual oficial

O FocusMind possui uma identidade visual já aprovada.

**Conceito da marca:**
- Logo principal com a letra F estilizada e um perfil humano integrado.
- Brilho representando pensamento, movimento e transformação.
- Símbolo F simplificado para ícones e aplicações reduzidas.
- Estética moderna, expressiva e minimalista.
- Preto profundo, branco e laranja vibrante.

**Paleta de referência:**
- Laranja principal: #FF702B
- Creme de apoio: #FFF7ED
- Escuro de apoio: #30231D
- Preto profundo como base visual.

**Nome:** FocusMind

**Slogan:** Evolua do seu jeito.

A identidade original deve ser preservada. Os arquivos gráficos aprovados serão adicionados posteriormente, sem substituição por logos provisórias.

## Roadmap de desenvolvimento

### V1 — Fundação e MVP

- [ ] Estrutura inicial do projeto
- [ ] Design system e componentes
- [ ] Login e cadastro
- [ ] Autenticação por Google, Apple, Facebook e e-mail
- [ ] Perfil do usuário
- [ ] FocusLearn: sessões e histórico de estudos
- [ ] FocusMove: atividades e registros
- [ ] FocusLevel: XP, níveis e conquistas
- [ ] FocusTeams: equipes, convites e feed
- [ ] Chat de texto e funcionalidades sociais básicas
- [ ] Testes de segurança e acessibilidade

### V2 — Comunidade e colaboração

- [ ] Salas de voz
- [ ] Sessões coletivas
- [ ] Desafios entre equipes
- [ ] Aprimoramento dos rankings e da moderação

### V3 — Inteligência e integrações

- [ ] Recomendações inteligentes
- [ ] Relatórios avançados
- [ ] Integrações opcionais com smartwatches
- [ ] Monitoramento inteligente de produtividade
- [ ] Personalização avançada da experiência

## Privacidade e segurança

O projeto deverá adotar boas práticas de segurança e proteção de dados, incluindo:

- Autenticação segura.
- Proteção das informações pessoais.
- Controle de privacidade dos perfis.
- Permissões para funcionalidades inteligentes.
- Possibilidade de exclusão de conta.
- Moderação e denúncia de conteúdos.
- Adequação à LGPD.
- Atenção especial à segurança de menores de idade.

Nenhum recurso de acompanhamento inteligente deverá ser obrigatório.

## Princípios do projeto

**Acessibilidade:** ferramentas úteis para pessoas com diferentes necessidades e experiências.

**Autonomia:** cada pessoa estabelece seu próprio ritmo.

**Evolução:** o progresso é individual, não uma competição obrigatória.

**Comunidade:** compartilhar conhecimento e crescer em conjunto.

**Tecnologia responsável:** funcionalidades inteligentes com transparência, segurança e controle do usuário.

## Origem do FocusMind

O projeto nasceu de conversas e reflexões sobre dificuldades de concentração, organização de estudos, motivação e desenvolvimento pessoal.

A ideia inicial de monitoramento inteligente dos estudos evoluiu para um ecossistema mais amplo, integrando educação, movimento, gamificação e comunidade.

**Idealização:** Abner Alencar.

**Colaboração nas ideias iniciais:** Adriano.

**Planejamento consolidado:** outubro de 2026.

[Documentação e planejamento no Notion](https://app.notion.com/p/31f0c2a5f910809ea41fdaf2f5c19c55)

## Desenvolvedores

O FocusMind está sendo desenvolvido por:

- **Abner Alencar** — Desenvolvedor
- **Marcelo Sanches** — Desenvolvedor

Juntos, trabalhamos para transformar o FocusMind em uma plataforma de evolução pessoal acessível, moderna e integrada.

## Licença

Ainda não definida. O projeto está em fase inicial de desenvolvimento e planejamento.

---

**FocusMind — Evolua do seu jeito.**
