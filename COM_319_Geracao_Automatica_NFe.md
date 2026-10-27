# COM 319 — Geração Automática de NF-e

> Fonte: Wiki Conexos (wiki.conexos.cloud/index.php/COM_319) — extraído em 27/10/2026

## Sobre a tela

A tela de **Geração Automática de NF-e (COM_319)** tem como finalidade centralizar o comando, a transmissão e o monitoramento de todas as Notas Fiscais Eletrônicas de Mercadoria (Modelo 55) da empresa. Ela atua como um "Cockpit de Mensageria", sendo essencial para:

- **Assinar e Transmitir** o XML das notas fiscais para a SEFAZ.
- **Monitorar o status** de autorização (Autorizada, Rejeitada, Denegada) em tempo real.
- **Atualizar o status do documento conforme retorno da SEFAZ.**
- **Tratar contingências**, permitindo ações de recuperação como:
  - Consultar recibos em caso de timeout;
  - Cancelar lotes travados;
  - Gerar XML para validação externa.
- **Integrar com terceiros**, permitindo a geração de arquivos XML para clientes (ex: Importação por Conta e Ordem) sem transmissão própria.

### Informações Importantes

#### Perfil de Usuário e Requisitos para Utilização da Tela

##### Público-alvo

Esta tela é voltada para profissionais que atuam, como:

- **Faturistas e Assistentes Fiscais:** Operam a tela diariamente para garantir que as notas saiam para o transporte.
- **Analistas de Suporte / TI:** Acessam para diagnosticar rejeições de XML, travamentos de lote ou falhas de comunicação com a SEFAZ.

##### Pré-requisitos

- **Status na Origem:** O documento deve estar com situação **"Homologado"** nas telas de origem (Fiscais de Entrada ou Fiscais de Saída). Documentos "Em Cadastro" não são listados aqui.
- **Série Fiscal:** O documento deve utilizar uma série configurada como **Eletrônica (Modelo 55)** na tela de Cadastro de Séries. Séries manuais (ex: Modelo 1) não passam por esta tela.
- **Certificado Digital:** Deve haver um certificado digital (A1) vigente e configurado na tela de Configuração de Certificados. Se o certificado estiver vencido, o serviço ficará indisponível.
- **Ambiente SEFAZ:** O envio respeitará estritamente o ambiente (Produção ou Homologação) definido na tela de Parâmetros da Filial. Não é possível alterar o ambiente diretamente nesta tela.
- **Serviço de Mensageria (Robô):** O agente de transmissão (NFeAgente) deve estar ativo e rodando no servidor.

#### Informações Técnicas

Consulte o detalhamento referente a campos, filtros e botões desta tela no Manual Técnico de Geração Automática de NF-e.

## Acessando a tela

Para acessar esta tela, dentro do Conexos Cloud, existe duas opções:

- No menu de telas acesse: **Faturamento / Transmissão NF-e > Geração Automática de NF-e**;
- No menu de busca, digite: **COM_319** (código da tela).

## Saiba mais

#### O Fluxo Assíncrono de Transmissão (Lote)

A COM_319 não transmite a nota em "tempo real" síncrono. Ela opera em um modelo **Assíncrono de Lotes**:

1. **Agendamento:** Quando você clica em Processar, o sistema cria uma tarefa na fila.
2. **Envio:** O Robô pega a tarefa, assina o XML e envia para a SEFAZ.
3. **Recibo:** A SEFAZ devolve um número de Recibo (confirmando recebimento, não validação).
4. **Consulta:** O Robô aguarda alguns segundos e consulta esse Recibo para saber se foi Autorizado ou Rejeitado.

**Por que isso importa?** Se a comunicação falhar entre o passo 2 e 3, a nota pode ficar travada como "Aguardando Retorno". Nesse caso, a nota pode já estar autorizada na SEFAZ, mas o sistema não sabe. **Nunca reenvie imediatamente**. Use a função "Consultar" para baixar o status real.

## Operando a Transmissão

### Fluxo Automático (Dia a Dia)

**Processar Lote**

- Selecione as notas pendentes na grid principal e clique no botão **PROCESSAR**.
- O sistema exibirá: "Tarefa agendada com sucesso".
- O robô executa a sequência: **Geração de XML > Geração de Lote > Transmissão > Consulta**.
- Acompanhe o status pela coluna "Situação". Se tudo der certo, ela mudará para **Autorizada** e o botão de **Imprimir** ficará habilitado.

### Fluxo Manual e Contingência (Mais Ações)

Ao lado do botão "Extrair Arquivos", o menu de "Mais Ações" permite controlar cada etapa individualmente para resolver problemas.

**Gerar XML (Validação Prévia)**

- Gera o arquivo XML assinado, mas **não transmite**.
- Use esta opção para exportar o arquivo e testar em validadores externos antes de tentar o envio oficial.

**Consultar**

- Força uma consulta direta à base da SEFAZ usando a chave de acesso.
- **Quando usar:** Essencial para casos de **Timeout** (Nota parada em "Processando" ou "Aguardando Retorno"). Se a nota já existir na SEFAZ, este botão baixa o protocolo e finaliza a nota no sistema, evitando duplicidade.

**Gerar NF de Terceiros**

- Gera o XML de uma nota de entrada (ex: Importação por Conta e Ordem) para envio ao cliente.
- **Diferencial:** O XML é gerado **sem assinatura digital** (o cliente deve assinar no sistema dele) e os dados do emitente (tag `<emit>`) são puxados do Cadastro de Processos, ignorando a filial logada.

### Correção de Erros (Gerência de Lote)

Se uma nota for rejeitada ou travar, ela fica bloqueada para edição na origem. Para corrigir, siga o roteiro:

**1. Validar Status**

- Confirme no Portal da SEFAZ que a nota **não** existe.

**2. Cancelar Lote**

- No menu flutuante **"G"** (lateral direita), localize o lote pendente e clique em **Cancelar Lote**.

**3. Cancelar XML**

- No menu "Mais Ações", clique em **Cancelar XML**.
- Agora o documento voltou para o status "Homologado" na tela de origem, permitindo edição.

### Regra Automática: Tag NatOp (Paraná)

Existe uma automação específica para notas de ajuste emitidas por filiais do Paraná (UF = PR).

- **Gatilho:** Notas marcadas como "NF de Ajuste" usando os CFOPs: **1949, 2949, 3949** (Entrada) ou **5949, 6949, 7949** (Saída).
- **Ação:** O robô preenche automaticamente a tag **NatOp** no XML com o valor: "Nota Fiscal de Estorno".
- **Motivo:** Regra de validação da SEFAZ/PR. O sistema sobrescreve qualquer descrição manual para evitar rejeição.

## Relatórios Relacionados

- **RP_COM_498 - Relatório Rejeição SEFAZ:** Este relatório é o "Debug Oficial" para as rejeições de soma (Erro 610/538). Ele compara o totalizador da nota com a soma dos itens e aponta exatamente qual campo (II, IPI, Despesas) tem a diferença de centavos que causou a rejeição.
- **RP_COM_232 - Detalhes NF-e:** Atua como um "Raio-X" da nota antes da transmissão. Lista produto a produto com os rateios de impostos e despesas aplicados, permitindo identificar erros de cálculo antes de gerar o XML.
- **RP_COM_326 - Espelho da Nota:** Utilizado para conferência visual (layout de DANFE) antes da emissão oficial.

## Robôs Relacionados

- **Robô de Transmissão (NFeAgente):** Responsável por ler a fila da COM_319, assinar o XML com o certificado, comunicar com o WebService da SEFAZ e processar o retorno. É monitorado pelo botão flutuante **"A" (Ações de Robô)**.
- **Robô de Consulta de Status:** Processo de fundo que verifica periodicamente se notas paradas em "Processando" já tiveram retorno da SEFAZ.

## FAQ

#### Consigo transmitir Notas Fiscais de Serviço (NFS-e) por esta tela?

**Não.** A tela **COM_319** é exclusiva para a transmissão de Notas Fiscais de Mercadoria (Modelo 55).

- Para notas de serviço, utilize as telas específicas de NFS-e (como Geração de NFS-e ou NFS-e Municipal), dependendo da integração com a sua prefeitura.

#### Como mudo o ambiente de transmissão para "Homologação" (Teste)?

A **tela** não possui botão para trocar de ambiente. Ela obedece estritamente a configuração global da Filial.

- Para alterar, acesse a tela de Parâmetros por Filial > Aba Faturamento e altere o campo "Ambiente NFe".
- **Atenção:** Isso afeta todas as notas emitidas pela filial.

#### Preciso enviar o XML para meu cliente emitir a nota (Conta e Ordem). Como faço?

Não utilize o botão "Processar".

1. Selecione a nota na grade.
2. Clique no menu **Mais Ações > Gerar NF de Terceiros**.
3. O sistema gerará o XML com os dados do Adquirente (Processo) como emitente e **sem assinatura digital**, pronto para envio por e-mail.

#### Percebi um erro na nota que já está nesta tela. Posso editar aqui?

**Não.** Esta tela é apenas um painel de envio.

- Se a nota já tiver XML gerado (status "Validada" ou "Erro"), você deve primeiro usar a opção **Cancelar XML** (em Mais Ações).
- Isso destrava o documento e permite que você o edite na tela de origem.

#### Por que minha Logomarca não aparece na impressão do DANFE?

Isso geralmente ocorre quando o endereço da filial é muito longo.

- O Manual da NF-e limita o cabeçalho. Se o endereço na tela Cadastro de Filiais tiver 75 caracteres ou mais, a logo é ocultada para não quebrar o layout.
- **Solução:** Abrevie o endereço da filial ou imprima o DANFE no formato **Paisagem**.

#### A nota sumiu da tela, mas não imprimi o DANFE. Onde ela está?

A COM_319 lista por padrão as notas pendentes. Se a nota foi Autorizada, ela pode ter saído da visão padrão dependendo do filtro.

- Verifique os filtros no topo da tela ou acesse a tela de origem (Fiscais de Saída), onde a nota estará com status **Finalizada** e o botão de impressão disponível.

## Status e erros

#### Mensagem: Lote Contábil sem Lançamentos

**Causa:** Na tela de Cadastro do CFOP no botão Contabilidade, não foram realizados as parametrizações contábeis corretas entre Débito/Crédito; ou O **Tipo de Operação** entre o Documento os encargos de contabilização são diferentes.

**Solução:** Deve entrar na tela de Cadastro de CFOP > Botão: Contabilidade, e promover a inclusão das contas contábeis entre Débito/Crédito; ou Validar qual é o tipo de operação correto a ser incluso, caso tenha necessidade de estar preenchido.

#### Mensagem: Erro Finalizando Documento: O endereço de cobrança está cancelado.

**Causa:** O motivo do erro é devido a configuração de documentos cadastrada na seguinte Tela: Cadastro de Cliente > Mais Ações > Comissão > Botão Documentos Financeiros.

**Solução:** Deverá acessar o cadastro da Pessoa do Documento e no caminho Cadastro de Cliente > Mais Ações > Comissão > Botão Documentos Financeiros, cancelar o registro existente e refazê-lo. Em seguida, na Tela Geração Automática de NFe, pesquisar o documento, marcá-lo e em Mais Ações > Situação NF-e - consultar o documento para que o mesmo seja finalizado. Por último, validar se o documento foi finalizar e se a comissão foi gerada corretamente.

#### Mensagem: Erro Finalizando Documento: O valor total do processo ultrapassa o valor estipulado na filial.

**Causa:** Este erro ocorre quando o valor da soma das NF's ultrapassa o valor informado no campo "Valor Máximo das Notas Fiscais de Saída do Processo" (tela de Parâmetros de Filiais > "Faturamento"). A rotina efetua a seguinte validação:

- Valor da nota atual + valores das demais NF's já finalizadas
- Se o somatório for maior que o valor informado no campo "Valor Máximo das Notas Fiscais de Saída do Processo", ocorre este erro.

**Solução:** Para resolução é necessário aumentar o valor estipulado na filial.

#### Mensagem: "Erro finalizando o retorno: ECNXEXECUTIONEXCEPTION: ERRO: PRODUTO NÃO CADASTRADO NO ESTOQUE FUTURO"

**Causa:** Na tela de Cadastro de Parâmetros da Filial na opção "GERAIS - ESTOQUE FUTURO" o campo "USAR ESTOQUE FUTURO" está definido como "Sim".

**Solução:** É necessário ir até o campo "USAR ESTOQUE FUTURO" e definir como "Não" e em seguida gerar novamente.

#### Mensagem: Erro finalizando o retorno: Valor quitado do adiantamento e valor vinculado a documentos é insuficiente para a baixa.

**Causa:** Este erro ocorre de forma automática devido um parâmetro na tela Cadastro de Parâmetros da Filial → Quadro Financeiro - Políticas Financeiras e Travas → Executar Permuta → Automática Adiantamento. Caso a opção **SIM** seja selecionada a rotina será executada quando um documento for finalizado na tela de fiscais de saída (retorno de autorização SEFAZ) e selecionando a opção **NÃO** a rotina não será executada.

**Solução:** Para resolução é necessário alterar o campo para "NÃO" e em seguida acessar: Geração Automática de NFe → Pesquisar o documento → Selecionar → Mais Ações → Situação NF-E → Consultar. Dessa forma o documento será finalizado e depois se desejar poderá retornar o campo para "SIM", após a finalização será possível utilizar o procedimento para a troca de condição de pagamento.

#### Mensagem: Erro finalizando retorno: O total dos valores baixados é maior do que em aberto no título

**Causa:** Este erro ocorre quando a soma dos encargos apresenta um valor diferente do esperado pelo título.

**Solução:** Para resolução considere a seguinte validação: Quando este erro ocorrer, deverá verificar qual a condição de pagamento cadastrada no documento (tela de Condição de Pagamento > Duplicatas (selecionar a informada no erro)) > campo "Descontar Despesas Pagas pelo Cliente". Se estiver como "SIM", o sistema irá realizar um somatório dos encargos que compõem o valor da duplicata (II, IPI, Seguro Internacional, outras despesas, Frete Internacional, COFINS Nacionalização, PIS Nacionalização, Desconto, Taxa Siscomex). Se o total for diferente do que é esperado pelo título, o erro será gerado, sendo necessário ajustar o campo "Descontar Despesas Pagas pelo Cliente" para "NÃO" e, posteriormente, acessar a tela de Geração Automática de NF-e > selecionar os documentos desejados > Mais Ações > Situação NF-e e consultar a situação do documento, para atualizar a situação.

#### Erro na execução do robô: ERROR EXECUTING TRANSACTION

**Causa:** Esse erro geralmente ocorre devido a instabilidade na comunicação com a SEFAZ. No entanto, também pode acontecer se o certificado na tela Gerência de Certificados estiver vencido.

**Solução:** Deverá acessar a tela de Gerência de Certificados e cadastrar um novo certificado para continuar com o faturamento.

#### Mensagem de Erro: "Erro - NFE: Rejeicao: informado codigo de beneficio fiscal incompativel com CSTE UF [NITEM:1]"

**Causa:** Ao emitir uma NF-e (modelo 55), o código de benefício fiscal (campo CBNEF) informado pode estar incompatível com o Código da Situação Tributária (CST) de acordo com a Tabela de Código de Benefício Fiscal por UF. Essa incompatibilidade resulta na rejeição pelo motivo 931.

**Solução:** Para resolver, é necessário corrigir o campo CBENEF cBenef, inserindo o código de benefício fiscal correspondente ao CST informado, conforme a tabela de códigos de benefício fiscal por UF. Além disso, verificar se o CST informado na nota fiscal está correto.

#### Mensagem de erro: The element 'imposto' in namespace 'http://www.portalfiscal.inf.br/nfe' has invalid child element 'IBSCBS'...

**Causa:** O erro ocorria devido aos cálculos envolvendo casas decimais, que não estavam fechando corretamente por causa da falta de precisão nos valores.

**Solução:** Ajustar os encargos de CBS/IBS para duas casas decimais, garantindo assim a precisão necessária para transmitir o documento com sucesso.

#### Situação de erro: Ao gerar XML de terceiros, os dados de ICMS não sendo levados para o CML em questão.

**Causa:** Ao gerar XML de terceiros, os dados de ICMS não são levados para o arquivo porque a inclusão da tag de ICMS depende do regime de tributação. Para XML normal, é considerado o campo "Regime Tributário da Empresa" na tela de Parâmetros da Filial. Já para XML de terceiros, o campo considerado é Apuração Fiscal, localizado no botão Documentos da tela Cadastro de Pessoas, vinculado ao processo. Se no cadastro da pessoa estiver marcado como SIMPLES e, no documento fiscal (telas de Fiscais de Entrada/Saída → aba Itens → botão Encargos, aba SPED/CST, campo CSO Simples Nacional) estiver definido como "-001 - NENHUM", a tag de ICMS não será inserida.

**Solução:** Validar se o campo Apuração Fiscal da pessoa está correto com a informação SIMPLES. Caso esteja correto, ajustar a parametrização do CFOP para que o valor adequado seja levado ao campo CSO Simples Nacional, garantindo a inclusão da tag de ICMS no XML.

#### Rejeição: Erro não catalogado

**Causa:** A unidade do produto na Nota Fiscal de Exportação não está de acordo com a NT 2016.001.

**Solução:** Ajustar o cadastro da Unidade do Item de acordo com a tabela disponibilizada na SEFAZ.

#### Rejeição 108: Serviço Paralisado Momentaneamente (Curto prazo)

**Causa:** Este retorno será apresentado quando o Webservice da Sefaz estiver parado por um curto prazo de tempo para realizar alguma manutenção ou alteração.

**Solução:** Neste caso deve-se aguardar o serviço voltar a disponibilidade e ir tentando a transmissão da NF-e. Talvez seja necessário entrar em contato com a SEFAZ para verificar o motivo da instabilidade e se será necessário entrar em contingência.

#### Rejeição 109: Serviço Paralisado sem Previsão

**Causa:** Este retorno será apresentado quando o Webservices da Sefaz estiver parado, para realizar alguma manutenção ou alteração, porém, irá levar um certo tempo para finalizar a manutenção, por este motivo, que é retornado sem previsão.

**Solução:** Talvez será necessário entrar em contato com a SEFAZ para verificar o motivo da instabilidade e se será necessário entrar em contingência.

#### Rejeição 203: Emissor não habilitado para emissão de NF-e

**Causa:** Este retorno será apresentado quando o Webservices da Sefaz quando o Emitente não estiver habilitado para emissão de NF-e.

1. Normalmente, empresas recente criadas e que ainda estão em processo de cadastramento na Sefaz;
2. Empresas que já são emissoras, porém estão com algum tipo de pendência na Sefaz ou Receita Federal;
3. Por falha na Sefaz.

**Solução:** Nessa situação, proceder da seguinte forma:

- Primeiro consulte a sua Inscrição Estadual ou CNPJ no SINTEGRA ou Cadastro Centralizado de Contribuintes (CCC). Ao fazer essa consulta, é possível verificar a situação cadastral da sua empresa e se encontra-se habilitada.
- Em todos os casos, é importante entrar em contato coma a Sefaz para verificar sua situação cadastral na Sefaz e o motivo da rejeição, este deve ser realizado pelo Setor Contábil/Fiscal da Empresa.
- Normalizado o problema, basta reenviar sua NF-e a partir do seu Software Emissor.

#### Rejeição 206: NF-e já esta inutilizada na base de dados da Sefaz

**Causa:** O número de uma determinada série fiscal que está sendo utilizado no faturamento em algum momento foi inutilizado.

**Solução:** Para confirmar a mensagem acima, deverá entrar no site do Portal Nacional da NF-e e através do link para fazer a consulta pesquisando ano a ano. Deverá utilizar um outro número/série fiscal para emissão da nota fiscal.

#### Rejeição 213: CNPJ-Base do emitente difere do CNPJ do Certificado Digital

**Causa:** Este erro ocorre pois o Certificado vinculado a filial na tela de Certificados não possui o mesmo CNPJ da filial logada e emissora da NF-e.

**Solução:** Instale o certificado digital correto e faça o processamento da nota novamente.

#### Rejeição 231: IE do emitente não vinculada ao CNPJ/CPF

**Causa:** Esta rejeição ocorre quando a inscrição estadual não está de acordo com a Sefaz.

**Solução:** Para resolução siga até a tela de Empresas / Filiais > campo "Documento Estadual" e realize o ajuste e fature o documento. Observação: Verifique o cadastro da pessoa da filial na tela de Cadastro de Pessoas > botão "Documentos" se está correto.

#### Rejeição 232: IE do destinatário não informada

**Causa:** Quando o for emitida uma NF-e para Destinatário, identificado como Isento (indIEDest = 2) ou Não Contribuinte (indIEDest = 9), que possui Inscrição Estadual (IE) ativa no seu Estado (UF) e essa não for informada em seus Dados, será retornado a rejeição "232 - IE do destinatário não informada".

**Solução:** Deverá efetuar uma consulta no 'Cadastro Centralizado de Contribuinte (CCC)' e verificar se este cliente tem IE (Inscrição Estadual) ativa. Em caso afirmativo, deverá ajustar o cadastro do cliente mediante os dados disponibilizados no CCC. OBSERVAÇÃO: Nos casos de clientes Isentos de Inscrição Estadual para o Estado de 'DF' o campo de I.E deve ser preenchido com o código CFDF.

#### Rejeição 233: IE do destinatário não cadastrada

**Causa:** Quando for emitida uma NF-e e a Inscrição Estadual do Destinatário (Campo: dest / IE - ID: E17) for válida e não estiver cadastrada na Sefaz Estadual, será retornando a rejeição "233 - IE do destinatário não cadastrada".

**Solução:** Deverá solicitar ao destinatário do documento fiscal que verifique junto ao Setor Contábil/Fiscal se foi realizado o cadastro no CCC. Inclusive a Sefaz RS dispõe de um site para consulta cadastral no CCC.

#### Rejeição 245: CNPJ Emitente não cadastrado

**Causa:** Quando for emitida uma NF-e e o CNPJ do emitente for válido e não estiver cadastrada na sefaz estadual, será retornada a rejeição.

**Solução:** Deve-se verificar se o CNPJ do emitente informado foi digitado correto e se existe cadastrado na sefaz. Consulte o seu CNPJ no sintegra ou no cadastro centralizado de contribuintes. Em todo caso, será necessário entrar em contato com a sefaz para verificar a situação cadastral do seu CNPJ e inscrição estadual. Normalizado sua situação cadastral junto a sefaz, basta reenviar a NF-e para processamento.

#### Rejeição 254: NF-e complementar não possui NF referenciada

**Causa:** Quando for emitida uma nf-e com finalidade de emissão (Campo: IDE / FINNFE - ID: B25) igual a "2 - NF-e complementar" e não for informado o grupo de documento fiscal referenciado (Campo: NFREF - ID: BA01) com uma NF-e, NFC-e ou NF modelo 1, será retornado a rejeição 254.

**Solução:** Deverá entrar na com_297 > botão mais ações > docs relacionados e informar o tipo se ENTRADA ou SAIDA e o código do documento.

#### Rejeição 268: NF complementar referencia uma outra NF-e complementar

**Causa:** Quando for emitida uma NF-e complementar referenciando outra NF-e complementar, será retornado a rejeição 268 - NF complementar referencia uma outra NF-e complementar".

**Solução:** Uma NF-e complementar pode referenciar uma NF-e com finalidade "1 - Normal", "3 - Ajuste" ou "4 - Devolução", mas nunca outra NF-e "2 - Complementar". Deve-se verificar a NF-e informada no grupo de documentos referenciados e substituir o documento informado pelo documento original e não outro documento complementar. Após ajustar o documento relacionado, basta reenviar a nota fiscal para a sefaz.

#### Rejeição 301: Uso denegado: Irregularidade Fiscal do Emitente - CNPJ XX.XXX.XXX/XXXX-XX

**Causa:** A Filial, emitente da nota fiscal, está com alguma irregularidade em sua Inscrição Estadual junto a SEFAZ.

**Solução:** Neste caso, a empresa emissora de NF-e/Filial, deverá entrar em contato com a SEFAZ estadual para verificar qual a pendência em relação a Inscrição Estadual. Após a confirmação de que não há mais irregularidades, tente novamente transmitir a nota fiscal.

#### Rejeição 302: Uso Denegado: Irregularidade Fiscal do Destinatário

**Causa:** O motivo do erro é alguma irregularidade do Destinatário junto a SEFAZ.

**Solução:** Neste caso, a empresa emissora de NF-e/Filial, deverá entrar em contato com o cliente/destinatário e informar que ao emitir a NF-e está retornado irregularidades junto a Sefaz. Após os ajustes por parte do destinatário, efetuar a transmissão da NF.

#### Rejeição 303: Destinatário não habilitado a operar na UF

**Causa:** O motivo do erro é alguma irregularidade do Destinatário junto a SEFAZ.

**Solução:** Neste caso, a empresa emissora de NF-e/Filial, deverá entrar em contato com o cliente/destinatário e informar que ao emitir a NF-e está retornado irregularidades junto a Sefaz. Após os ajustes por parte do destinatário, efetuar a transmissão da NF.

#### Rejeição 306: IE do Destinatário não está ativa na UF

**Causa:** Este erro ocorre quando for emitida uma NF-E (Modelo 55) e a situação do destinatário no CCC (Cadastro Centralizado de Contribuientes) estiver como "Não Habilitado", haverá rejeição pelo motivo 306 - IE do Destinatário não está ativa na UF.

**Solução:** O emitente de uma NF-e rejeitada pelo código de retorno 306 nada pode fazer para corrigir a situação. O código de retorno diz respeito a uma irregularidade no CNPJ do destinatário. O emitente pode orientar o seu cliente a entrar em contato com a Sefaz para regularizar a sua situação.

#### Rejeição 321: NF-e de devolução de mercadoria não possui documento fiscal referenciado

**Causa:** Este erro ocorre, pois está sendo gerada uma NF de Devolução. No manual da Sefaz, menciona ser necessário referenciar o documento que está sendo devolvido.

**Solução:** Caso a NF esteja com situação 'Em Homologação', para ajustar, deverá edita-la. O documento fiscal que está sendo devolvido, deve ser informado na seguinte tela: VERSÃO CLOUD:

- Esta tela é válida para Documentos de Entrada e Saídas.
- Fiscais de Entrada > Botão Mais Ações > Opção Doc. Relacionados > Quadro Documento Retorno
- Fiscais de Saída > Botão Mais Ações > Opção Doc. Relacionados > Quadro Documento Retorno

#### Rejeição 327 e 328: CFOP inválido para NF-e com finalidade de devolução de mercadoria

**Causa:** A crítica é referente ao CFOP utilizado no documento, pois não está conforme o manual da SEFAZ.

**Solução:** Será necessário verificar o cadastro do CFOP informado na NF e ajustar conforme Manual do Contribuinte disponibilizado pela SEFAZ. No Manual do Contribuinte consta o Anexo XIII - CFOP Específico > Anexo XIII.01 - CFOP de Devolução de Mercadoria, neste constam os CFOP's considerados para NF's de devolução. Além do manual do contribuinte também devem ser verificados 2 pontos:

- No CFOP deve estar configurado na aba Avançados Devolução = Sim.
- O documento fiscal estar lançado como Tipo = Retorno.

#### Rejeição 331: Informar o CNPJ do adquirente ou do encomendante nesta forma de importação

**Causa:** O erro ocorre quando na emissão de uma NF-e de importação (MOD.55), dentro do grupo declaração de importação (DI), a tag "Forma de Importação Quanto a Intermediação" (TPINTERMEDIO) for igual a [2 - Importação por Conta e Ordem] ou [3 - Importação por Encomenda] é obrigatório o preenchimento da tag CNPJ do adquirente ou do encomendante (CNPJ) informando os zeros a esquerda também.

**Solução:** Para solucionar o erro é necessário validar se no campo "Encomendante/Adquirente" no cadastro do processo está informada uma pessoa física, caso não esteja, uma outra opção é alterar o tipo do processo para "Conta Própria"

#### Rejeição 332: CNPJ do adquirente ou do encomendante da importação inválido

**Causa:** Este erro ocorre quando na emissão de uma NF-e d importação (mod.55), dentro do grupo Declaração de Importação (DI), a informação contida na tag CNPJ do adquirente ou do encomendante (CNPJ) é inválida. (zeros, nulo ou DV inválido).

**Solução:** Para correção do erro é necessário validar o cadastro da pessoa encomendante/adquirente no cadastro do processo vinculado ao documento e averiguar se o CNPJ informado é válido.

#### Rejeição 340: Não informado o grupo de exportação indireta no item

**Causa:** Alguns dos campos listados abaixo não estão preenchidos devidamente: Aba processo > Campo Finalidade = Exportação. Aba logística > Quadro Exportação - Local de Embarque > Campos UF /Local. CFOP iniciado com 7. Preenchimento botão exportação na linha do item.

**Solução:** Validar se os campos acima estão preenchidos com as informações corretas nas telas de Cadastro do Processo e Fiscais de Saída.

#### Rejeição 346: Somatório das quantidades informadas na Exportação Indireta não corresponde a quantidade total do item

**Causa:** O erro ocorre por que na nota fiscal de exportação foi informada uma quantidade no item diferente da quantidade informada no botão exportação da linha do item, assim, a quantidade da nota fiscal vinculada fica diferente da nota fiscal de exportação.

**Solução:** Validar a quantidade informada nos itens da nota fiscal de exportação e a quantidade informada no botão exportação na linha dos itens.

#### Rejeição 351: Valor do ICMS da operação no CST=51 difere do produto BC e alíquota da SEFAZ

**Causa:** Na validação BC de ICMS, %percentual ICMS e valor ICMS, em um determinado produto a tag `<VBC>` não está sendo gerada pois na tela Classificador de Produtos > Campo "Incentivos Fiscais" > Crédito Tributário = NÃO.

**Solução:** Deverá alterar na Tela COM_007 (Classificador de Produtos) > Campo Incentivos Fiscais > Crédito Tributário = SIM e refaturar a ODF.

#### Rejeição 354: Informado grupo de devolução de tributos para NF-e que não tem finalidade de devolução de mercadoria

**Causa:** Quando for emitida uma NF-E (modelo 55) com a finalidade de emissão diferente de devolução (FINNFE <> 4) e informado o grupo de devolução de tributos (GRUPO: DET/IMPOSTODEVOL), haverá a rejeição pelo motivo 354.

**Solução:** Para que possa emitir esta NF-e, deverá proceder da seguinte forma:

1. Cancelar o documento (se via procedimento NF-e de Ajuste ou editar a NF-e)
2. Ajustar no CFOP O campo DEVOLUÇÃO = NÃO
3. Regerar o documento ou homologá-lo
4. Em seguida transmitir o documento.

#### Rejeição 355: Informar o local de saída do país no caso da exportação

**Causa:** Este erro ocorre porque no Cadastro do Processo, Aba Logística, não foi informado o local de embarque no quadro Exportação – Local de Embarque.

**Solução:** Ajustes a serem efetuados na tela de Cadastro do Processo:

1. Aba processos > campo **Finalidade**: deve ser **Exportação**.
2. Aba logística > campo **Exportação - Local de Embarque**: deve incluir informação no e regerar a Nota Fiscal.

#### Rejeição 377: Código de País do destinatário inexistente

**Causa:** Este erro ocorre quando for emitida uma NF-e e o código do país (cPaís) do destinatário não existir na tabela de países divulgados pela Sefaz.

**Solução:** Deve-se consultar a tabela de países divulgada pela Sefaz e localizar o código correspondente ao país do destinatário da NF-e. Feito isso, vá até a tela Países e inclua o código no campo "BACEN".

#### Rejeição 388: Código de Situação Tributária do IPI incompatível com o Código do Enquadramento Legal do IPI

**Causa:** Este erro ocorre porque no Cadastro de CFOP, Aba SPED / NF-e, foi informado um Enquadramento Legal do IPI que não condiz com o CST do item.

**Solução:** Deve verificar junto ao setor fiscal qual o Enquadramento legal do IPI correto e ajustar a informação no CFOP.

#### Rejeição 444: Valor do ICMS não corresponde à base de cálculo x alíquota

**Causa:** Esta rejeição ocorre quando for emitida uma NF-e (modelo 55) e o valor do ICMS (campo: vICMS) tiver um valor diferente do esperado do calculado do valor base vezes(X) a alíquota.

**Solução:** Para resolução, deve ser verificado se o cálculo realmente está correto. Primeiramente deve validar se as informações do Valor de Base de Cálculo (vBC) e Alíquota do ICMS (pICMS) estão corretos. vBC: É considerado o valor do Produto (vProd); pICMS: Valor da alíquota de ICMS do produto, em %. Pode ser obtida com o contador de sua confiança. Com as informações acima validadas, é feito o cálculo do Valor do ICMS: vBC * (pICMS/100) = vICMS. Após validar as informações devem ser feitos os ajustes no Conexos para assim, reenviar a NF-e para autorização.

#### Rejeição 471: Informado NCM=00 indevidamente

**Causa:** Na tela de Cadastro de Produto > Campo: Tipo, a opção utilizada esta incorreta, o que acaba ocasionando o erro.

**Solução:** Na tela de Cadastro de Produto > Campo: Tipo, ajustar para a opção **Produto de Revenda**, por exemplo.

#### Rejeição 479: Data de Emissão anterior a data de credenciamento ou anterior a Data de Abertura do estabelecimento

**Causa:** O erro ocorre ao emitir uma NFe com o campo dhEmi_B09= AAAA-MM-DDThh:mm:ss com uma data anterior ao que a sefaz liberou o seu credenciamento ou anterior a data de abertudo do estabelecimento.

**Solução:** Neste caso, deverá solicitar ao Setor Contábil/Fiscal que valide todos os cadastros / credeciamentos necessários junto a Sefaz Ambiente Nacional e Sefaz da UF na qual está inscrito.

#### Rejeição 506: Data de saída menor que a data de emissão

**Causa:** Esta rejeição é em relação a Data de Saída x a Data de Emissão do documento junto a Sefaz.

**Solução:** Para solucionar esta rejeição, deverá proceder da seguinte forma:

1. Verificar se há lote ou xml gerado e cancelar.
2. Se via pedido de vendas:
   - Cancelar o documento
   - E ao faturar o pedido de venda novamente, ajustar as datas na Tela de Faturamento de Pedidos de Venda.

#### Rejeição 508: CST incompatível na operação com Não Contribuinte

**Causa:** Esta rejeição ocorre ao emitir uma NF-e com o campo IndIEDest=9, não contribuinte do ICMS, e o campo CST do ICMS receber um valor diferente de 00, 20, 40, 41, 60.

**Solução:** Para resolução, deverá validar internamente junto ao Setor Contábil/Fiscal qual o CST que se adequa ao tipo de operação. Realizado o ajuste no CST/CFOP, efetue o passo a passo abaixo:

1. Cancelar a NF
2. Cancelar a programaçao do Pedido de Venda
3. Estornar o Pedido de Venda
4. Excluir e inserir os itens novamente
5. Finalizar o Pedido de Venda e Gerar a Programação
6. Faturar o Pedido de Venda
7. Transmitir e Homologar a NF

#### Rejeição 525: CFOP de Importação e não Informado Dados da D.I.

**Causa:** Quando for emitida uma nf-e com CFOP iniciado por 3, indicando uma operação com o exterior (IDDEST = 3) e de entrada (TPNF = 0), e não for informado o grupo de declaração de importação (DI), será retornado a Rejeição 525.

**Solução:** Deverá informar os dados da D.I. ou emitir a nota fiscal com um dos CFOP's da lista de exceções da SEFAZ. Ou verificar se o processo é referente a Faturamento Courrier. Em caso afirmativo, gentileza acessar o manual Faturamento Courrier e proceder conforme orientações.

#### Rejeição 527: Operação de Exportação com informação de ICMS incompatível

**Causa:** Quando for emitida uma NF-e de saída de Exportação, CFOP iniciando com 7 e o código CST for diferente de 41 ou CSOSN diferente de 300 (NT 2010/010).

**Solução:**

- Verificar no botão encargos dos itens qual o código CST foi gerado
- Ajustar no Cadastro de CFOP para o CST 41 - Não tributada
- Volte na NF-e, nos Encargos dos itens, e clique no **botão Calcular** para que a CST seja ajustada no documento.

#### Rejeição 529: CST incompatível na operação com Contribuinte Isento de Inscrição Estadual

**Causa:** Quando for emitida uma NF-e com Identificação do Destinatário (Campo: dest / indIEDest) como "2 - Contribuinte Isento de Inscrição Estadual" e o CST do ICMS for "50 - Suspensão na cobrança do ICMS" ou "51 - Diferimento na cobrança do ICMS", será retornado a rejeição 529.

**Solução:** Para ICMS com Suspensão ou Diferimento na cobrança somente é permitido para Destinatário com identificado como "Contribuinte do ICMS" (indIEDest = 1). Logo, para corrigir essa rejeição, deve-se informar o Destinatário da NF-e como Contribuinte do ICMS e sua Inscrição Estadual, mas caso o Destinatário da NF-e seja realmente "Contribuinte Isento", deve-se escolher tributação adequada para esse tipo de Destinatário.

#### Rejeição 532: Total do ICMS difere do somatório dos itens

**Causa:** Esta mensagem foi apresentada quando foi tentado faturar uma nota fiscal com CST de ICMS 30. No caso deste CST não se calcula ICMS, pois é Isento ou Não tributado, porém calcula-se ICMS Substituição. Desta forma, ao tentar fazer a nota fiscal deduzindo o ICMS Normal do ICMS ST, que seria o cálculo tradicional, é apresentado o erro.

**Solução:** Deve-se retirar a dedução do ICMS Normal do ICMS Substituto, ou seja, para usar o CST 30 deverá ser realizado o cálculo Base de ICMS ST * % ICMS ST.

#### Rejeição 533: Total da BC ICMS-ST difere do somatório dos itens

**Causa:** O motivo do erro é devido ao cálculo do encargo referente ao **BASE ICMS ST**. O encargo pode estar com valor errado; e/ou negativo; e/ou sem valor. Assim, acaba não fechando com o valor esperado pela SEFAZ.

**Solução:** Para solucionar este erro e transmitir o documento, deverá ser validado o seguinte:

1. O percentual de referente a Base do ICMS ST
2. O valor do encargo Base do ICMS ST

#### Rejeição 534: Total do ICMS-ST difere do somatório dos itens

**Causa:** O motivo do erro é devido ao cálculo do encargo referente ao **ICMS ST**. O encargo pode estar com valor errado; e/ou negativo; e/ou sem valor. Assim, acaba não fechando com o valor esperado pela SEFAZ.

**Solução:** Para solucionar este erro e transmitir o documento, deverá ser validado o seguinte:

1. O percentual de referente a ICMS ST
2. O valor do encargo ICMS ST

#### Rejeição 539: Duplicidade de NF-e com diferença na Chave de Acesso

**Causa:** A Sefaz esta emitindo este erro porque já existe uma nota fiscal registrada com a chave mencionada no erro e a mesma série da nota que esta tentando transmitir.

**Solução:** Deverá proceder da seguinte forma:

- Acessar o emissor NF-e e efetuar a Consulta da Situação NF-e
- Ou consultar a série da nota fiscal da Tela Cadastro de Séries Fiscais, pesquisar a série da nota fiscal e mudar a informação do campo de sigla para impressão no livro fiscal para alguma diferente das demais séries. Depois deverá fechar, reabrir as telas e tentar transmitir de novo a nota.

#### Rejeição 578: A data do evento não pode ser maior que a data do processamento

**Causa:** Esta rejeição normalmente ocorre quando há diferença entre os horários do servidor de emissão da nf-e com relação horário do servidor da Sefaz.

**Solução:** Deverá ajustar o horário na máquina de emissão da NF-e e no servidor. Normalmente, atrasar o horário em alguns minutos para ficar abaixo do que consta no servidor da Sefaz funciona e a emissão de NF-e volta ao normal.

#### Rejeição 599: CFOP de Importação E não informado dados de II

**Causa:** Quando for emitida uma NF-e com CFOP iniciado por 3, indicando uma Operação com o Exterior (idDest = 3) e de Entrada (tpNF = 0), e não for informado o Grupo do Imposto de Importação (II), será retornado a rejeição "599 - CFOP de Importação e não informado dados de II".

**Solução:** Deve-se informar o Grupo de Imposto de Importação para corrigir essa rejeição.

#### Rejeição 602: Total do PIS difere do somatório dos itens sujeitos ao ICMS

**Causa:** O item da nota fiscal deve estar com CST de PIS = 04 'Operação Tributável Monofásica - Revenda Alíquota Zero'. Isso faz com que sejam geradas as tags 'PISNT' ou 'PISOUTROS' e/ou 'COFINSSNT' ou 'COFINSOUTROS' no item, porém, o valor de PIS e COFINS tributados também são somados nas tags respectivas do 'ICMSTOT', ocorrendo a Rejeição 602 e/ou 603.

**Solução:** Na tela de Cadastro de CFOP > Aba: Avançados, deve validar o CST informado no campo PIS. Provavelmente a configuração desse campo não está corretamente parametrizado. Ou validar a tela de CST por NCM para todas as NCM dos produtos que constam no faturamento.

#### Rejeição 610: Total da NF difere do somatório dos Valores compõe o valor Total da NF

**Causa:** A configuração do CFOP utilizado no faturamento está incompatível com a regra da SEFAZ.

**Solução:** Deverá validar as configurações do CFOP utilizado no faturamento e efetuar os ajustes necessários, para que seja atendida a regra. Vale notar que o Valor do Produto no sistema é formado pelos encargos que estão configurados para Ratear ao Valor da Mercadoria. IMPORTANTE: Caso o documento gerado seja referente a **NF-e de Ajuste**, deverá seguir os passos:

1. Utilizar o relatório **RP_COM_498** (Relatório Rejeição Sefaz - 610) para verificar os valores divergentes (não aceitos pela Sefaz).
2. Identificado os valores divergentes, cancelar o documento.
3. Gerar novo documento, observando os filtros do procedimento (Zerar valor FRETE INTL, SEGURO INTL, II, PIS/COFINS, Tag Voutros).

#### Rejeição 611: CEAN INVÁLIDO

**Causa:** Essa rejeição ocorre quando for emitida uma NF-e e o Código de Barras do Produto (tag: cEAN) informado for inválido ou estiver ausente. Quando informado números no campo cEAN e houver esta rejeição, significa que o último número do sequencial não é válido (dígito verificador).

**Solução:** Para resolução, acesse a tela de Cadastro de Produtos > Aba: "Unidades" e faça os ajustes necessários na coluna "Código de Barras".

#### Rejeição 629: Valor do produto difere do produto valor unitário de comercialização e quantidade comercial

**Causa:** Foi emitida uma NF-e / NFC-e com Valor Unitário de Comercialização multiplicado pela Quantidade Comercial resultando em um Valor do Produto diferente do calculado.

**Solução:** Deve-se verificar e refazer a multiplicação entre os Campos qCom e vUnCom de cada item da NF-e / NFC-e e corrigir o Valor do Produto. Há uma tolerância para mais ou para menos de R$ 0,01 de diferença do valor calculado sem aproximações. Deve ser validado as limitações de casas decimais na tela de Cadastro de CFOP e também dentro do botão 'Encargos' coluna 'Precisão'.

#### Rejeição 630: Valor do Produto difere do produto Valor Unitário de Tributação e Quantidade Tributável

**Causa:** O erro em questão ocorre quando:

- O Valor do Produto oriundo da multiplicação (produto) entre o Valor Unitário de Tributação e a Quantidade Tributável for diferente do esperado. Como por exemplo, Zero na coluna Valor Unitário Trib; ou
- Quando a sigla da unidade, sendo levada para o XML nas TAGs `<UCOM>` E `<UTRIB>`, forem inválidas.

**Solução:** Neste caso, deverá rever os valores no documento fiscal:

- QTD TRIB
- UNIDADE TRIB
- VALOR UNITARIO TRIB

Se por ventura os valores dos campos citados estiverem nulos/vazios/zeros, deverá validar o cadastro do produto o campo QTD TRIB. Caso não tenha informação deverá ajustar.

#### Rejeição 663: Alíquota do ICMS com valor superior a 4 por cento na operação de saída interestadual com produtos importados

**Causa:** A causa da Rejeição (663) é devido a Alíquota do ICMS com valor superior a 4 por cento na operação de saída interestadual com produtos importados será apresentada quando:

- IE do destinatário difere de ISENTO ou nulo;
- O CFOP de operação de saída para outra UF iniciar com o número 6;
- A origem da mercadoria (orig_N11) = 1, 2 ou 3;
- O CST de ICMS (CST_N12) = 00, 10, 20, 70 ou 90;
- Valor alíquota do ICMS maior do que 4.00% (4 por cento).

**Solução:** Para efetuar os devidos ajustes, proceder conforme descrito abaixo:

- Deverá validar as configurações do CFOP utilizado no faturamento e efetuar os ajustes necessários, para que seja atendida a regra.
- Verificar se a NCM, está configurada corretamente no Classificador de Produto e seu respectivo percentual do ICMS.
- Se as informações da Origem da Mercadoria foram devidamente configuradas no sistema nas seguintes Telas: Classificador de Produto, Cadastro de Produto e Tipo de Operação.

#### Rejeição 679: Chave de acesso referenciada com modelo inválido

**Causa:** Foi vinculado ao Botão: Logística > Aba: Doc. Relacionados, um documento na qual o modelo da chave de acesso é diferente de 55.

**Solução:** Deverá confirmar se a chave de acesso da nota referenciada do documento vinculado esta correto. Caso contrário deverá retirar o vinculo com este documento.

#### Rejeição 680: Duplicidade de NF-e referenciada (Chave de acesso referenciada mais de uma vez)

**Causa:** No lançamento da nota fiscal foram vinculados mais de um documento referenciado. Essa situação geralmente ocorre em notas fiscais complementares, devido a necessidade de informar o documento na qual esta sendo complementado.

**Solução:** Deverá ser preenchido na tela Fiscais de Saída > Mais Ações > Botão Docs. Relacionados somente um dos campos:

- COM_297 > Mais Ações > botão "Docs. Relacionados" > campo "Nota Mãe"
- COM_297 > Mais Ações > botão "Docs. Relacionados" > campo "Documento Retorno"

#### Rejeição 694: Grupo de ICMS Interestadual para a UF de Destino deve ser informado na Operação Interestadual de Venda a Consumidor Final

**Causa:** Este erro ocorre quando, ao emitir uma NF-e (Modelo 55) para acobertar uma operação interestadual com consumidor final e não contribuinte, não sendo uma prestação de serviços, e não for informado o grupo do ICMS para a UF de destino, retornará a rejeição 694.

**Solução:** Para resolução, deverá informar o grupo de ICMS para a UF de destino da NF-e. Essa configurações estão disponíveis no manual de **Configuração ICMS em Operações Interestaduais**.

#### Rejeição 695: Informado indevidamente o Grupo de ICMS para UF de Destino

**Causa:** Quando for emitida uma NF-e e PELO MENOS UMA das situações abaixo estiverem descritas na Operação da NF-e e FOR INFORMADO o Grupo de ICMS para a UF de Destino (ICMSUFDest), será retornado a rejeição "695 - Informado indevidamente o grupo de ICMS para a UF de destino". (Ex: Operação Estadual, Consumidor Normal, Operação com Contribuinte).

**Solução:** De acordo com as causas acima, os campos no cadastro de pessoas e cadastro de cfop devem ser validados. O Tipo de Contribuinte deve ser validado no Cadastro de Pessoas > Botão: Documentos > Campo: Inscrição Estadual. O Tipo de Consumidor deve ser validado no Cadastro de CFOP > Campo: Consumidor Final.

#### Rejeição 696: Operação com Não Contribuinte deve indicar operação com Consumidor Final

**Causa:** A pessoa do Documento é do Tipo: Não contribuinte, porém o Cadastro do CFOP está configurado para pessoa Contribuinte.

**Solução:** Deverá ajustar o Cadastro do CFOP > Aba: Básicos > Campo: Consumidor Final para SIM.

#### Rejeição 697: Alíquota interestadual do ICMS com Origem Diferente do Previsto

**Causa:** Se emitida uma NFe com o valor do campo **PICMSInter** igual a 4% e a Origem da Mercadoria for incompatível (0, 4, 5, 6, 7) OU igual a 7% ou 12% e Origem incompatível (1, 2, 3, 8).

**Solução:** Para corrigir o documento, deverá solicitar que o Setor Contábil/Fiscal valide a origem da mercadoria conforme o percentual do encargo **PICMSINTER**.

#### Rejeição 699: Percentual do Icms Interestadual para UF de destino difere do previsto para o ano da data de emissão

**Causa:** Esse erro ocorre, pois o encargo referente ao percentual de ICMS interestadual (PICMSINTERPART - ICMS INTERESTADUAL PROVISORIO DE PARTILHA) para o ano em que está sendo emitida a nota fiscal, é diferente do percentual que está sendo informado no encargo da NF.

**Solução:** Deverá ajustar o percentual do encargo no CFOP. O percentual a ser ajustado é referente ao ICMS InterEstadual para UF de destino (Parâmetros Tributários > Campo ICMS INTERESTADUAL PROVISORIO DE PARTILHA).

#### Rejeição 703: Data-Hora de Emissão posterior ao horário de recebimento

**Causa:** As informações de Data/Hora presentes no XML que está sendo transmitido, estão adiantadas em relação à Data/Hora da SEFAZ. Geralmente essa situação ocorre devido ao horário de Verão.

**Solução:** É necessário ajustar no servidor para posteriormente tentar a transmissão novamente.

#### Rejeição 732: CFOP de Operação Interestadual e IDDEST diferente de 2

**Causa:** Para esta situação, trata-se de um documento de Entrada. Exemplo: A filial pertence ao estado de SC e a pessoa do documento também pertence ao estado de SC. Para a operação foi utilizado um CFOP 2XXX, ou seja, um CFOP de retorno para operação interestadual.

**Solução:** Para conseguir fazer a emissão da NF-e sendo Pessoa da Filial e Pessoa do Documento do mesmo estado, porem utilizando CFOP interestadual, deve acessar o botão Logística > Aba: Retirada e informar a pessoa e o endereço. Esta pessoa informada na aba retirada, deverá pertencer a uma UF diferente das demais pessoas.

#### Rejeição 733: CFOP de operação interna e idDest diferente de 1

**Causa:** O erro ocorre devido a seguinte validação da SEFAZ: CFOP de Operação Interna (inicia por 1 ou 5) e IDDEST <> 1. (UFs do Remetente e Destinatário iguais + CFOP iniciado com 5 + Existe endereço de entrega caracterizando operação interestadual).

**Solução:** Neste caso, deverá verificar junto ao Setor Contábil/Fiscal qual o CFOP adequado para o documento em questão. Após validar o CFOP, deverá proceder com o passo a passo abaixo:

- Cancelar o XML.
- Editar a NF.
- Se for gerado via ODF, cancelar a NF, ajustar o CFOP e refaturar a ODF.
- Se for NF manual, editar a NF, excluir os itens, inserí-los novamente com o CFOP correto.
- Se for via Pedido de Venda, cancelar a NF, cancelar a Programação, estornar o Pedido de Venda, ajustar o CFOP e refazer os demais lançamentos.

Por último, efetuar a homologação do documento e transmitir.

#### Rejeição 787: NF-E com indicativo de NFC-e com Entrega a Domicilio

**Causa:** Através da tela de documento (Entrada/Saída) > Botão: Mais Ações > Opção: Logística > Campo: Presença do comprador, foi informado a opção: NFC-e em operação com entrega a domicílio.

**Solução:** Como no Conexos, atualmente, não temos operação de NFC-e, uma opção que pode ser configurada no campo de presença do comprador é: Operação não presencial, Outros.

#### Rejeição 778: Informado NCM inexistente

**Causa:** Quando for emitida uma NF-e e o NCM (Nomenclatura Comum do Mercosul) não existir na tabela de NCM publicada pelo Ministério do Desenvolvimento, Indústria e Comércio Exterior - MDIC, será retornado a rejeição.

**Solução:** Deve-se consultar a tabela disponibilizada pelo Ministério do Desenvolvimento, Indústria e Comércio Exterior - MDIC para confirmar a existência do Código NCM informado. Na maioria dos casos, assim como a rejeição informa, realmente não existe o código informado e nesse caso, é necessário identificar outro código NCM, existente, previsto e que melhor se enquadra na sua Operação. Efetuado os ajustes com relação a NCM correta para a operação, basta refaturar e tentar novamente homologar a NF-e.

#### Rejeição 805: A SEFAZ do destinatário não permite Contribuinte Isento de Inscrição Estadual

**Causa:** Quando for emitida uma NF-e com a Identificação da IE (indIEDest) como "2 - Contribuinte Isento de Inscrição Estadual" em Estado (UF) que não permite essa identificação da IE em Operações Internas / Estaduais (idDest = 1) ou Operações Interestaduais (idDest = 2), será retornado a rejeição "805". Os Estados que não permitem que os destinatário tenham indicação como Contribuinte Isento são: AM, BA, CE, GO, MG, MS, MT, PA, PE, RN, SE, SP.

**Solução:** Para efetuar a transmissão da NF-e, deverá proceder da seguinte forma:

1. Verificar a UF da pessoa do documento, se o mesmo está nestas UF's (AM, BA, CE, GO, MG, MS, MT, PA, PE, RN, SE, SP.)
2. Em caso afirmativo, acessar Cadastro de Cliente > Botão Documentos e se no campo Doc. Estadual estiver escrito, **Isento (a)**, apagar, salvar.
3. Transmitir o documento novamente.

#### Rejeição 815: Valor do ICMS Interestadual para UF de Destino difere do calculado

**Causa:** Quando for emitida uma NF-e com o Valor do ICMS Interestadual para a UF de Destino (vICMSUFDest) diferente do Calculado pela Sefaz, será retornado a rejeição "815".

**Solução:** Configurar o CFOP de forma que o cálculo do ICMS de destino fique de acordo com a validação 815 da Sefaz. Para corrigir a sua NF-e, você deve refazer o cálculo de todos os itens que estiverem com o Valor do ICMS para a UF de Destino incorreto.

#### Rejeição 817: Unidade Tributável Incompatível com o NCM Informado na Operação com Comércio Exterior

**Causa:** Esta rejeição é referente a Nota Técnica 2016/001 - Unidade de Medida Tributável por NCM para Exportações. O motivo de apresentar a mensagem de rejeição é porque, de acordo com a planilha de **Unidade Tributada** para as Operações com Comercio Exterior da NT2016.01, a unidade tributada utilizada para a **NCM** está diferente do esperado pela **SEFAZ**.

**Solução:** Sendo assim, deverá efetuar os devidos ajustes no sistema:

1. Na Tela Cadastro de mercadorias da TEC validar se a informação na COLUNA UNIDADE está correta com o esperado pela SEFAZ.
2. Em casos de NF gerada a partir do **Procedimento Gerar NFE de Ajuste**, antes de homologar o documento, deverá proceder da seguinte forma:
   - Cancelar o documento de ajuste gerado.
   - Gerar um novo com status **EM CADASTRO**
   - Consultar o documento
   - Alterar o Tipo de **Retorno para Corretiva**: este é obrigatório, pois os produtos não consideram os dados da unidade tributável, este deve ser informado manualmente.
   - Incluir as informações: **QTD. TRIB., UNIDADE TRIB**.
   - Retornar o Tipo do Documento para Retorno.
3. Caso não esteja, deverá efetuar os devidos ajustes e homologar o documento novamente.

#### Rejeição 845: O Grupo Transportador não pode ser preenchido para a modalidade do frete informada

**Causa:** Esta rejeição ocorre quando na(s) tela(s) de Fiscais de Entrada/Fiscais de Saída (Botão "Mais Ações" > Logística) o campo "Tipo Frete" esteja configurado igual a "Sem Transporte", e no quadro "Transportadora" seja informado o Transportador.

**Solução:** Para resolução, deverá ajustar o campo "Tipo Frete" para a opção correta ou retirar a transportadora informada.

#### Rejeição 850: Data de vencimento da parcela não informada ou menor que a data de vencimento da parcela anterior

**Causa:** Essa validação da Sefaz passou a ocorrer na versão 4.0 da NFE. Uma das causas desta validação estar ocorrendo pela a Sefaz é pelo o fato da data de vencimento da última parcela ser menor que a data de vencimento da parcela anterior.

**Solução:** Deverá ajustar a ordem da condição de pagamento, porém, se esta já tiver sido utilizada em um outro título e que está finalizado, não conseguirá ajustar ela e deverá utilizar outra condição que atenda a exigência da Sefaz.

#### Rejeição 852: Número da parcela inválido ou não informado

**Causa:** Esta é uma nova validação da Sefaz em relação a ordenação das duplicatas no DANFE e no XML.

**Solução:** Caso ocorra este erro, deverá verificar no XML gerado, se as tags abaixo foram geradas e na sequência:

- `<dup>` 001
- `<dup>` 002
- Se de 001 saltar para 003, por exemplo, o erro irá ocorrer.

#### Rejeição 865: TOTAL DOS PAGAMENTOS MENOR QUE O VALOR TOTAL DA NOTA

**Causa:** O VALOR DO DOCUMENTO COM_009 ESTÁ DIFERENTE DO VALOR DO TITULO COM_009 > BOTÃO FINANCEIRO > CAMPO TÍTULOS. ESTA É UMA EXIGENCIA DA VERSÃO 4.00 DA NF-E.

**Solução:** VERIFICAR NA TELA COM_009 > BOTÃO PROPRIEDADES > ABA PROPRIEDADES > CAMPO NF-E > SE ESTA CONFIGURADO O CAMPO 'ENVIA DUPL NFE' = SIM. COMO SUGESTÃO DE SOLUÇÃO, É ALTERAR A CONDIÇÃO DE PAGAMENTO DA TELA CMN_019 PARA QUE GERE TITULOS QUE FECHEM COM 100% DO TOTAL DA NF-E TELA.

#### Rejeição 868: Grupo transportador, veículo transporte e reboque não devem ser informados

**Causa:** Esta mensagem é apresentada quando a nota fiscal é emitida para um destinatário fora do estado do emitente e foram inserido informações de Placa e UF no Quadro: Transportadora > Botão: Logística.

**Solução:** Através do Botão Logística > Quadro: Transportadora, deve-se deixar em branco a informação do Campo: Placa e Campo: UF.

#### Rejeição 882: GTIN (CEAN) com prefixo inválido

**Causa:** O código GTIN informado na aba Unidades na tela de Cadastro de Produtos possui prefixo inválido de acordo com o país.

**Solução:** No manual de NFe, é orientado a utilizar o site (https://www.gs1.org/standards/id-keys/company-prefix) para identificar qual seria o prefixo correto. Ou seja, o GTIN informado no cadastro do produto não está de acordo com o esperado pela Sefaz e é preciso corrigir tomando como base o site indicado.

#### Rejeição 863: Total do IPI devolvido difere do somatório dos itens

**Causa:** Quando for emitida uma NF-e (modelo 55) e o total do IPI devolvido, calculado no grupo de totais da NF-e (Campo: total / ICMSTot / vIPIDevol - ID: W12a), for diferente do somatório do IPI devolvido dos itens. Geralmente estas divergências estão relacionadas a arredondamentos e ou conversões de casas decimais.

**Solução:** Deve validar se no cadastro do CFOP e no botão Encargos possuem configuração de precisão para realizar os cálculos. Além disso, deve verificar se o CFOP que está sendo utilizado, está na lista de CFOPs de Devolução que consta no manual de Orientação do Contribuinte. No CFOP deve validar a Aba: Avançados > Campo: Devolução.

#### Rejeição 898: Data de vencimento da parcela não informada ou menor que Data de Autorização

**Causa:** Esta rejeição é em relação a Data de Vencimento da Duplicata x a Data de Autorização do documento junto a Sefaz.

**Solução:** Para solucionar esta rejeição, deverá proceder da seguinte forma:

1. Verificar se há lote ou xml gerado e cancelar.
2. Editar a nf-e se foi gerada manualmente ou via ODF.
   - Se via ODF, cancelar, ajustar as datas e refaturar
   - Se gerada manualmente, ajustar as datas e refaturar.
3. Se via pedido de vendas:
   - Cancelar o documento
   - E ao faturar o pedido de venda novamente, ajustar as datas na Tela de Faturamento de Pedidos de Venda.

#### Rejeição 930: CST com benefício fiscal e não informado o código de benefício fiscal

**Causa:** Quando for emitida uma NF-e (modelo 55) ou NFC-e (modelo 65) e não informado o código de benefício fiscal (Campo: cBenef) para CST - Código da Situação Tributária (Campo: CST - Grupo N) que exige o código de benefício fiscal, haverá a rejeição pelo motivo 930.

**Solução:** Para solucionar esta rejeição, deverá proceder da seguinte forma:

1. Acessar o manual da Tela Cadastro de Observações do CFOP
2. Proceder com o cadastro orientado na respectiva tela
3. Se for ODF, refaturar a ODF
4. Se for Pedido de Venda, cancelar NF e faturar o pedido novamente
5. Se for manual, editar nf-e, excluir o item e lançá-lo novamente.

#### Rejeição: IE do destinatário não está ativa na UF, porém, em consulta ao Sintegra o cliente da nota fiscal está ativo.

**Causa:** O erro ocorre devido a alguma irregularidade no CNPJ/IE do destinatário.

**Solução:** Entre em contato com seu cliente solicitando que o mesmo verifique com sua contabilidade se há alguma pendência junto a SEFAZ que precise ser regularizada.

#### Rejeição 843: Código da espécie de veículo incompatível com o tipo do veículo.

**Causa:** O código da espécie do veículo informado na tela Cadastro de Produtos é incompatível com o tipo do veículo.

**Solução:** Para a resolução do erro é necessário seguir as seguintes instruções:

1. Baixar a tabela no portal da nota fiscal eletrônica.
2. Verificar o tipo do veículo no sistema e localizá-lo na tabela.
3. Verificar quais são as espécie compatíveis com o tipo do veículo informado no sistema e ajustar a informação da espécie no sistema.
4. Após o ajuste, cancelar o documento através do botão "Cancelar NF", dentro da ODF (Ordem de Faturamento) e refaturar a ODF.
5. Transmitir o documento gerado e homologado através da tela Geração Automática de NF.

#### Rejeição 974: CNPJ do responsável técnico diverge do cadastrado.

**Causa:** Ao realizar uma emissão de uma NF-e ou NFC-e com o CNPJ do responsável técnico (Conexos) que não corresponde ao CNPJ correto registrado na Sefaz ocorre a rejeição. Isso ocorre devido a atualização na Sefaz do Paraná, onde está sendo necessário realizar novo credenciamento vinculando o CNPJ da empresa ao CNPJ do sistema emissor de NF-e.

**Solução:** Para resolução, caso sua empresa seja do estado do Paraná, é necessário que seja realizado o credenciamento na SEFAZ/PR, utilizando o CNPJ da Conexos. Assim que for concluído o credenciamento, nossa equipe terá um prazo de **24 horas úteis** para realizar a **liberação** e, após isso, poderá ser emitida as notas fiscais pois o credenciamento estará concluído.

#### Rejeição 999: Erro não catalogado (informar a mensagem de erro capturado no tratamento da exceção)

**Causa:** Esta rejeição ocorre, na maioria das vezes, por alguma falha, indisponibilidade ou intermitência na Sefaz. O motivo "999" é um retorno genérico para uma falha que não possui uma mensagem padrão mapeada, ou para exceções e falhas na aplicação da Sefaz. Normalmente esse retorno acaba por indicar que a Sefaz está indisponível ou se ficará em breve.

**Solução:** Para resolução, deve acionar a Sefaz para verificar o motivo do problema. Outra alternativa é aguardar a normalização, pois em quase todos os casos, a mesma NF-e que foi rejeitada por este erro apresentado (999|Rejeição: Erro não catalogado), ao ser reenviada a Sefaz, é autorizada. Caso confirmado a indisponibilidade da Sefaz, pode-se, ainda, ativar a contingência para a emissão.

#### Rejeição: CVC-COMPLEX-TYPE.2.4.B: THE CONTENT OF ELEMENT 'CONSRECINFE' IS NOT COMPLETE...

**Causa:** Este erro é gerado por lentidão no processamento do lote pela Sefaz, causando um erro na consulta da situação da nota fiscal.

**Solução:** Acesse o portal da Sefaz e consulte a chave da nota fiscal, identificada nas telas de Fiscais de Entrada ou Fiscais de Saída, confirmando que a nota fiscal está autorizada (não estando, deve cancelar o Lote, o XML e retransmiti-la). Em seguida, acesse a tela de Geração Automática de NF-e e localizar o documento. Em seguida, clique no botão "Mais Ações" > botão "Situação NF-E" > botão "Consultar". Após o término da tarefa, verifique que o documento foi finalizado.

#### Rejeição: ERRO – NF-e 15427: TOTAL DA BC DO IBS E DA CBS DIFERE DA SOMA DOS ITENS.

**Causa:** Esta rejeição ocorre devido a diferenças de arredondamento no cálculo das casas decimais, fazendo com que o total da base de cálculo do IBS e da CBS não corresponda exatamente à soma dos valores calculados nos itens da nota fiscal.

**Solução:** Acesse a tela CFOP e clique no botão "Encargos". Edite os encargos de base de IBS/CBS e os encargos de IBS e CBS, ajustando o campo "Precisão" para 2 casas decimais. Após o ajuste, refature a ODF. Caso o documento tenha sido lançado manualmente, será necessário excluir o documento e lançar os produtos novamente, garantindo que os cálculos sejam refeitos com a precisão correta.

#### Logomarca não gera no danfe

**Causa:** A impressão correta da logomarca no DANFE no formato retrato depende dos dados cadastrais da empresa constam na tela Cadastro de Filiais.

- Com até 74 caracteres, a logo seria exibida / impressa no DANFE.
- Com 75 caracteres ou mais, a logo não será impressa no DANFE.

**Solução:** A opção nestes casos é:

1. Ou diminuir a quantidade de caracteres do endereço para no máximo 75 caracteres;
2. Ou utilizar/imprimir o DANFE no formato paisagem.

#### Erro gerando protocolo: erro carregando arquivo: Arquivo:"C:\conexosphoenix\bin\lllxgyseaa_.pdf não encontrado.

**Causa:** O erro ocorre devido ao sistema não estar localizando a **Impressora Conexos (bullzip)** instalada na máquina utilizada.

**Solução:** É necessário instalar a impressora de **PDF Bullzip**, e renomeá-la para "conexos".

#### Gerar Tag XML pRedBC

**Informação:** Para que o sistema gere informação na Tag do XML da NF-e `<pRedBC>` é necessário que o encargo referente a base de cálculo do ICMS que está configurado na tela GER_047 seja configurado como **Crédito Tributário = SIM**.

#### Mensagem de Erro: "Identificação do adquirente invalida"

**Causa:** O erro se refere ao documento federal do consignatário, que quando preenchido com um **CPF** ocasiona o erro. visto que, a informação do documento do consignatário é levada para o XML na tag `<numeroconsignatario>` e o campo no Siscomex para onde esta informação da tag é levada espera a informação de um **CNPJ**.

#### Erro Validando Arquivo Xml - Xbairro

**Causa:** O motivo do erro é devido que para o destinatário da NF, o Bairro deve ter no mínimo 2 caracteres e no máximo 60 caracteres de tamanho, conforme definição do manual do contribuinte.

**Solução:** Para ajustar o erro em questão:

1. Acesse a Tela Cadastro de Pessoas
2. Botão Endereço
3. Cancele o endereço e cadastre um novo corrigindo a descrição do bairro.
4. Em seguida, ajustar através do Botão Contabilidade a sequência do endereço antes de transmitir o documento no Emissor NF-e.

#### Erro Gerando XML - Gerando EMIT/C16: Fone

**Causa:** O erro citado acima pode ocorrer em duas situações:

- Porque no cadastro da filial Cadastro de Filiais não existe a informação do telefone de contato.
- Ou na geração do XML na seguinte rotina: Tela Geração Automática de NF-e > Mais ações > Gerar NF de Terceiros.

**Solução:** Se o documento for gerado pela Tela Geração Automática de NF-e > Mais ações > Gerar NF de Terceiros, deverá proceder com os ajustes abaixo: Acesse a Tela Cadastro de Pessoas, pesquise a pessoa desejada e insira o número de telefone no campo 'Telefone' da aba dados básicos. Deverá inserir o telefone no endereço da pessoa (Cadastro de Pessoas > Botão Endereço). Em seguida, prossiga com a geração do XML novamente. Caso contrario, deve inserir o número de telefone no cadastro da filial Cadastro de Filiais e tentar a transmissão da NF-e novamente.

#### Erro Gerando XML - Gerando EMIT/C01

**Causa:** O erro ocorre porque o cadastro da filial Cadastro de Filiais deve estar completo, ou seja, todos os campos preenchidos.

**Solução:** Deve realizar a configuração completa da filial, ou seja, preencher todos os campos.

#### Erro Gerando XML - Gerando DET_PROD/I01

**Causa:** Este erro ocorre quando existe produtos na nota fiscal sem a informação de NCM.

**Solução:** Deve verificar o cadastro de todos os produtos que fazem parte do faturamento na tela Cadastro de Produtos e Serviços e conferir se possuem a informação no campo NCM.

#### Erro Gerando XML - Gerando DET_PROD/I01 (Descrição Complementar)

**Causa:** Este erro ocorre quando o sistema não considera a descrição complementar do produto para o arquivo XML.

**Solução:** Deve verificar a Configuração de Descrição de Produtos na NF-e se estão devidamente configurados conforme as devidas orientações.

#### Erro Gerando XML - Gerando IPITRIB/O07

**Causa:** O erro ocorre porque as configurações relacionadas ao encargo de IPI estão incorretas no CFOP.

**Solução:** Deve-se avaliar se há valor e percentual para os encargos de base de IPI e valor de IPI, se está configurado como crédito tributário = sim, se na aba avançados o campo livro fiscal está = sim e configuração de CST e enquadramento de IPI.

#### Erro Gerando XML - Gerando PISOUTR/Q05

**Causa:** Com base no schema disponibilizado pela sefaz, quando configurado para levar CST 71, 72 e 74 é obrigatório informar: Se não for pauta: BC PIS / COFINS, % PIS / COFINS, Valor PIS / COFINS. Se for pauta: Qtd. BC, Qtd. %, Valor. Mesmo que o valor do encargo esteja igual a zero.

**Solução:** Deverá incluir no CFOP os encargos de BC PIS / COFINS as respectivas alíquotas e efetuar o lançamento dos itens novamente para que busque as novas configurações.

#### Erro Gerando XML - Gerando DET_PROD_DI/I18

**Causa:** Este erro ocorre porque a URF de despacho do BL não possui informação da UF na tela Cadastro de URF ou o BL está sem informação de URF Despacho.

**Solução:** Deverá incluir a informação de UF na URF utilizada no conhecimento de transporte ou incluir a URF Despacho no BL.

#### Erro Gerando XML - Gerando ICMSUFDEST/NA01

**Causa:** O erro é apresentado porque na configuração do CFOP o campo consumidor final está configurado = SIM, dessa forma, espera-se que nos encargos do CFOP tenha configuração para cálculo do diferencial de alíquota para consumidor final.

**Solução:** Deve verificar se é realmente uma operação para consumidor final e verificar a configuração do campo no CFOP. Caso seja operação para consumidor final, deverá configurar os encargos com os mesmos informados na tela Cadastro de Parâmetros de Filiais - Tributário, aba Trib. III. Além de validar o CFOP, verificar a inscrição estadual do destinatário, pois caso esteja como isento (a), o erro poderá ocorrer.

#### Erro: {"http://www.portalfiscal.inf.br/nfe":nre}' is expected

**Causa:** O erro é apresentado devido a falta de informação no campo Número do RE no Botão Exportação da Tela Fiscais de Saída.

**Solução:** Após lançar o item da NF, caso seja uma exportação, deverá informar o Número do RE no botão exportação.

#### Erro Validando Arquivo Xml - Ufterceiro

**Causa:** O motivo do erro é devido que no campo Encomendante Adquirente na Tela Cadastro de Processo está com informação de uma pessoa do exterior e não uma pessoa nacional.

**Solução:** Para ajustar o erro em questão:

1. Acesse a Tela Cadastro de Processo
2. Ajuste o campo Encomendante Adquirente, salvar
3. Editar a NF-e
4. Homologar novamente e transmitir

#### Erro Validando Arquivo Xml - nSeqAdic

**Causa:** O motivo do erro é devido a coluna Item na Tela IMP_002 > Aba Mercadorias. Na Coluna foi informado o código do produto, sendo que deve ser um número sequencial (1, 2, 3...).

**Solução:** Deverá proceder da seguinte forma:

1. Editar a NF-e (Fiscais de Entrada)
2. Na tela IMP_002, cancelar a NF
3. Na Aba Mercadorias, clicar no excluir itens
4. Na aba Mercadorias, clicar no incluir itens
5. Inserir os itens/quantidades desejas e confirmar.
6. Em seguida, faturar a odf.

#### Erro referente: Motivo: O elemento '{http://www.portalfiscal.inf.br/nfe}cExportador' não é esperado.

**Causa:** O erro ocorre por que na linha do item foi inserida informações de D.I./Adição/Seq. do item da D.I., logo, é esperado que exista informação do exportador.

**Solução:**

- Normalmente nestes caso o lançamento não é feito por ODF. Nestes casos em específico deverá acrescentar o processo no cabeçalho da nota e posteriormente relançar os itens, caso tenha lançado de forma manual.
- Ou retirar as informações de D.I. dos itens.

Obs.: Deverá verificar internamente junto ao setor fiscal/contábil qual das 2 opção irá optar.

#### Erro referente: Falha da análise do elemento {http://www.portalfiscal.inf.br/nfe}fone.

**Causa:** O telefone cadastrado no **botão endereços** da tela Cadastro de Pessoas da pessoa do faturamento está incorreto devido a validação da Sefaz.

**Solução:** 1- Acessar o cadastro da pessoa do faturamento, botão endereços, cadastrar e/ou copiar o endereço, corrigir a informação do telefone e depois apagar o endereço que está cadastrado de forma incorreta.

#### Erro referente: Falha Da Análise Do Elemento '{http://www.portalfiscal.inf.br/nfe}Serie' Com Valor 'Nf'.

**Causa:** O Modelo Fiscal selecionado para a série do documento e para o tipo de documento está diferente do que foi utilizado na nota fiscal original (vinculada no botão logística).

**Solução:**

- Efetuar os ajustes na série que foi selecionada no documento. Ou seja nos campos Modelo e no campo Sigla para Impressão no Livro Fiscal, selecionar o mesmo modelo e a mesma sigla que a nota fiscal original.
- Também ajustar a coluna Modelo Fiscal do tipo de documento que foi selecionado na nota para o mesmo modelo que foi selecionado na nota fiscal original ou 55 (que é o modelo para nota fiscal eletrônica exigido pela Sefaz).

#### Erro referente: Erro gerando XML: is not a valid integer value.

**Causa:** Este erro normalmente ocorre por que foram digitadas letras em um campo numérico. Também pode ocorrer por não informar a **via de transporte** na tela LOG_012 em um faturamento vinculado a processo.

**Solução:** Informar a via de transporte na tela LOG_012 e transmitir a NF-e novamente.

#### Erro referente: Falha da análise do elemento '{http://www.portalfiscal.inf.br/nfe}xPed'

**Causa:** Esse erro ocorre, pois no campo 'Pedido Cliente NR' do Pedido de Venda foi informado mais caracteres do que o permitido pela Sefaz ou porque foi informado alguma caractere especial, por exemplo 'em Branco' (foi dado espaço).

**Solução:** Para efetuar a correção, seguir os passos abaixo:

1. Cancele a NF gerada (Botão Propriedades da COM_009)
2. Cancele a programação do pedido
3. Estorne o pedido
4. Apague o item
5. Altere a informação do campo 'Pedido Cliente Nr' do pedido. Feito isto, refaça o faturamento.

#### Erro referente: Falha da análise do elemento '{http://www.portalfiscal.inf.br/nfe}Orig' com valor '6'.

**Causa:** A SEFAZ está validado o dígito da origem da mercadoria. Está sendo enviado 6, porém é esperado o valor 0, 1 ou 2.

**Solução:** Deve ser validado de onde está vindo a origem da mercadoria e ajustar para alguma das opções mencionadas pela SEFAZ, sendo: 0, 1 ou 2.

#### Erro referente: Falha da análise do elemento '{http://www.portalfiscal.inf.br/nfe}CST' com valor '73'.

**Causa:** Está sendo enviado para a SEFAZ a informação de CST 73 dos impostos de PIS/COFINS, porém está sendo esperado 99.

**Solução:** Nos casos de PIS/COFINS quando ausentes, deve validar a configuração no Cadastro do CFOP > Aba: SPED/NFE > Campo: PIS e Campo: Cofins. Deve validar junto ao setor Contabil/Fiscal se a CST configurada esta correta. Caso contrário, deverá ajustar.

#### Erro referente: Falha Da Análise Do Elemento '{http://www.portalfiscal.inf.br/nfe}xCpl' Com Valor ... Viola A Restrição Maxlength De '60'.

**Causa:** O erro é referente ao endereço da pessoa da nota fiscal, se observar o complemento do endereço, ele está com informações a mais do que a Sefaz permite, que são apenas 60 caracteres.

**Solução:**

1. Acessar o Cadastro da Pessoa da nota fiscal.
2. No Botão Endereço do Cadastro da Pessoa, localizar o CNPJ informado na NF.
3. Cancelar o que tem o complemento grande.
4. Duplicar e ajustar o campo complemento e marca-lo como padrão.
5. Editar a Nota Fiscal.
6. Acessar o Botão Contabilidade.
7. Buscar o CNPJ da pessoa e atualizar o endereço.
8. Salvar.
9. Homologar a nota e transmitir.

#### Erro referente: yErrText=Gerando ICMSUFDest/NA01.

**Causa:** Na configuração dos encargos do CFOP não foi configurado o encargo referente ao parâmetro da tela Encargos por Filial > Aba: Trib. III > Campo: ICMSUFDest

**Solução:** Configurar no cadastro do CFOP os encargos para atender Nota Técnica 2015 003.

#### Mensagem de Erro: Erro Validando Arquivo Xml - Modelo

**Causa:** Esse erro pode ocorrer por alguns motivos, como:

1. A nota fiscal que está sendo devolvida (documento de retorno vinculado no botão logística) foi emitida com uma série fiscal que não está cadastrada no Sistema.
2. Outro motivo é a séria fiscal já está cadastrada no sistema, porém ela não está configurada com o modelo '55'.
3. Ou ainda, a nota fiscal não possuir a chave de acesso vinculada no botão propriedades.

**Solução:** Para cada item acima, temos as soluções abaixo:

1. Cadastrar a série fiscal na tela Séries Fiscais
2. Informar o modelo 55 na tela Séries Fiscais
3. Inserir a chave de acesso no documento de retorno no botão propriedades da tela Fiscais de Saída

#### Mensagem de Erro: Código CEST não informado

**Causa:** O produto não possui "CEST" informado.

**Solução:** Deverá informar o "CEST" na tela de Cadastro de Produto (aba "Cadastro" > sub-aba "VI-Fiscal" > campo "ICMS/CEST").

#### Mensagem de Erro: Número de série inválido

**Causa:** No cadastro da tela de séries fiscais o campo ***modelo*** foi configurado como 002, por exemplo.

**Solução:** Ajustar o campo ***modelo*** para ter a informação 2.

#### Erro referente: Motivo: O encargo está com valor negativo.

**Causa:** Este ocorre quando o encargo que está gerando valor negativo é considerado no xml da NF-e.

**Solução:** Deverá ser verificado qual o encargo que está gerando valor negativo e efetuar os devidos ajustes.

#### Erro referente: Motivo: A data de fabricação do lote está incorreta.

**Causa:** Este ocorre quando a data de fabricação do lote está lançada incorreta. Exemplo: Data incorreta: 02/02/**0219**

**Solução:** Deverá ser verificado em Cadastro do Produto > Botão Lotes/Séries > Detalhamento da Mercadoria, se a data de fabricação está lançada correta. Caso não esteja, deverá cancelar o registro e lançá-lo novamente.

#### Erro referente: Motivo: Ausência de CNPJ ou número incorreto.

**Causa:** Este erro ocorre quando na tela Cadastro de Pessoas, botão "Documentos", campo "Documento Federal" o número do CNPJ estiver incorreto ou em branco.

**Solução:** Valide o número na tela Cadastro de Pessoas e valide novamente.

#### Erro: Cadastro de Produtos: O CFO selecionado está configurado para utilizar outro armazém.

**Causa:** Este erro ocorre devido à configuração de CFOP na tela CFOP → Acordeon Estoque → **Campo "Armazém Origem"** estando em branco sendo que o campo "Tipo Armazém Origem" é definido como obrigatório.

**Solução:** Para resolução do problema é necessário verificar com o setor Contábil/Fiscal a possibilidade de ajustar o campo "Tipo de Armazém Origem" para sugestivo invés de obrigatório assim, o campo "Armazém Origem" ficará disponível para ser inserido como qualquer armazém no documento. Também é possível alterar a informação do campo "Armazém Destino" para o "Armazém Origem" caso este armazém seja sempre utilizado.

#### Mensagem de Erro: "CVC-PATTERN-VALID... IDESTRANGEIRO... IS NOT VALID"

**Causa:** Ao tentar transmitir nota fiscal de entrada de importação, sistema apresenta a mensagem de erro na geração do XML. O erro ocorre porque no cadastro do endereço da pessoa do documento > campo **"Nº doc. exterior (TIN)"** foi preenchido com uma informação inválida.

**Solução:** Deverá cadastrar um novo endereço e deixar o campo mencionado acima em branco. Depois disso, atualize o endereço no processo, na Invoice e na ODF. Refature a ODF e seguir com a emissão da nota.

#### Mensagem de Erro: "ERRO NA TAREFA: 'NÃO FOI POSSÍVEL INICIAR O ROBÔ: FALHA NA COMUNICAÇÃO RPC..."

**Causa:** Este erro ocorre quando o robô utilizado não estava na versão do Java atualizado, gerando incompatibilidade nos dados e assim apresentando o erro.

**Solução:** Deve ser instalada a versão atualizada do Java, para isso o usuário deverá excluir a versão anterior e em seguida reiniciar o computador.

#### Mensagem de Erro: Erro transmitindo nota: O servidor enviou o código de status 403: Forbidden.

**Causa:** O erro ocorre devido a problemas na validação do certificado utilizado na transmissão de dados ao robô. Quando há incompatibilidades entre os dados do certificado e os utilizados na transmissão, o erro é gerado.

**Solução:** É necessário garantir que o certificado digital utilizado na transmissão esteja correto e válido. Certifique-se de que o CPF ou CNPJ do responsável no certificado seja o mesmo indicado na tag "CPFCNPJ" > "Remetente do XML de envio" e após isso atualize o certificado digital para que o CNPJ informado no certificado coincida com o remetente da NF.

#### Mensagem de Erro: ERRO GERANDO XML: NO ENUM CONSTANT BR.INF.PORTALFISCAL.XSD.ENUMS.TUF.1

**Causa:** Este erro ocorre pois, ao tentar transmitir o documento, há uma informação incorreta no campo "UF" da placa do veículo na tela de Fiscais de Saída.

**Solução:** Para resolver este erro, é necessário acessar a tela de Fiscais de Saída, clicar no botão "Logística", selecionar "Transportadora" e verificar o campo "Placa Veículo" e o campo "UF". Se o campo "UF" estiver com a informação "1", deve-se alterar para a sigla correta do estado, por exemplo, "SP".

#### Erro enviando documento para homologação: O campo série da NF-e referenciada não pode ser nulo.

**Causa:** O documento referenciado através do Botão Logística > Aba: Doc. Relacionado > Quadro: Doc. Relacionado ou Botão: Detalhes, foi lançado sem ser informado o campo: Série.

**Solução:** Deve procurar o documento referenciado através da tela de Fiscais de Entrada ou Fiscais de Saída e pelo Botão: Contabilidade, deve preencher o campo Série.

#### Erro Consultado Lote: Conexos_DataX.

**Causa:** O erro apresentado não é erro do sistema. Neste caso, falta espaço na tablespace do banco de dados, ou seja, a tablespace **CONEXOS_DATAX** está com uso de 100%.

**Solução:** Para solucionar o erro em questão, deverá solicitar ao DBA da empresa para aumentar o espaço em disco.

#### Mensagem apresentada (ERRO): Erro finalizando retorno: O valor indicado é maior do que em aberto no título ! Documento -> XXXX. Valor baixa: 39,570.91. Valor título: 36,527.00

**Causa:** O erro ocorre por que o valor do título no **botão financeiro** da tela COM_297 é R$ 3.047,86 e o desconto cadastrado no **botão descontos** para o cliente do faturamento está com valor maior R$ 4.571,79.

**Solução:** Normalmente quando ocorre esse erro, a nota fiscal é transmitida e autorizada na Sefaz, porém não é finalizada no Conexos. Para conseguir finalizar a nota no Conexos, deverá seguir os seguintes passos:

1. Deverá acessar a tela Fiscais de Saída > Mais Ações > Botão Descontos e alterar o status para cancelado;
2. Acessar a Tela Cadastro de Pessoas > Mais Ações > Botão Desconto e cancelar o registro.
3. Acessar a Tela COM_319 e em Mais Ações > Situação NF-e > Consultar o documento para que o mesmo seja atualizado.
4. Refazer o desconto no Cadastro da Pessoa.

#### Erro: O título código 1 está em situação com bloqueio de estorno/cancelamento.

**Causa:** Na tela de Situação de Duplicatas a coluna: Bloqueia Doc. está configurado como **SIM**.

**Solução:** Deverá **INATIVAR** o registro e criar um novo com a coluna: Bloqueia Doc. **NÃO**.

#### Erro: CONEXOS.PCK_NF_UTIL

**Causa:** O erro pode ter ligação com o fechamento inesperado da conexão no envio do lote.

**Solução:** Deve-se observar os flags marcados no emissor. Caso esteja marcado até lote e apresentar o erro poderá efetuar os passos a seguir:

1. Excluir lote;
2. Cancelar o XML;
3. Editar o documento;
4. Homologar o documento;
5. Transmitir para a sefaz novamente.

#### Erro transmitindo lote: Erro validando XML recebido: Inválido no nível superior do documento

**Causa:** O erro pode ter ligação com o certificado que esta instalado no emissor, pois ele pode estar vencido.

**Solução:** Deverá verificar com o setor responsável para efetuar a renovação do certificado e incluir um novo. Após a inclusão do certificado poderá retransmitir a nota fiscal.

#### Erro: Erros na transmissão do lote (TIMEOUT / SOAPFAULT)

**Causa:** Estes erros ocorrem pois excedem o tempo limite de transmissão do documento fiscal para a Sefaz.

**Solução:** Para que seja possível efetuar a transmissão do documento novamente, deverá proceder com o passo a passo abaixo:

1. Primeiramente consultar a chave de acesso vinculada ao documento no Site da SEFAZ para confirmar que a nota não foi transmitida.
2. Na Tela Geração Automática de NFe verificar se houve geração de XML e Lote. Em caso afirmativo, proceder da seguinte forma:
   - No menu flutuante (canto superior direito da tela), clicar em **GERÊNCIA DE LOTE**
   - Identificar o lote vinculado ao documento
   - Clicar em editar lote
   - Cancelar o lote gerado.
3. Na Tela Geração Automática de NFe > Botão Mais Ações > Cancelar XML, para cancelar o XML gerado.
4. Desta forma o documento estará disponível na Tela Fiscais de Saída para editar e realizar os ajustes caso necessário para transmitir o documento novamente.

#### Erro: Erro homologando documento: Erro enviando documento para homologação: Os campos pessoa e endereço do intermediador da transação não podem ser nulos.

**Causa:** O erro ocorre porque o campo "Presença do Comprador" no botão "Logística" da tela Logística está com preenchido a opção "Operação não Presencial, Outros".

**Solução:** Marque a opção "Não se Aplica" e valide.

#### Erro: Geração Automática de NF-e - Não é possível agendar uma nova tarefa com um lote que foi gerado em uma tarefa concluída com erros.

**Causa:** Este erro ocorre quando o documento não está registrado na Sefaz.

**Solução:** Para resolução siga o passo a passo:

1. Tela de Geração Automática de NFe → Menu flutuante > Gerência de Lote > Localize o lote do XML vinculado ao documento desejado > Cancele o lote.
2. Tela de Fiscais de Entrada → Botão "Mais Ações" > "Fiscal" > Cancelar NF-e gerado
3. Tela de Geração Automática de NFe → Pesquisar o documento em questão > Processe novamente o documento.

#### Erro gerando a tarefa: "Erro vinculando a tarefa ao robo: Já existe tarefa em execução para a entidade selecionada."

**Causa:** O erro é apresentado no histórico de agendamento do robô de importação de D.I e isso ocorre ao consultar uma D.I. que já esteja sendo consultada em outra tarefa.

**Solução:** Não há o que possa ser feito pelo lado do Conexos, pois trata-se de uma restrição no PUCOMEX sobre o limite de acessos de um mesmo IP, também podendo ocorrer pelo limite de consultas de um certificado. Somente é necessario cautela, para não exagerar na quantidade de agendamentos/consultas realizadas por dia.

#### Mensagem apresentada (ERRO): Erro inserindo NFe no lote: O tamanho do lote não pode exceder 490K

**Causa:** O lote de transmissão referente ao documento excedeu o tamanho 490k exigidos pela Sefaz. Isso porque o documento possui uma quantidade de itens ou descrição dos produtos muito grande, que consequentemente torna o arquivo de transmissão muito grande.

**Solução:** Deverá realizar a divisão da quantidade de itens em documentos diferentes. Por exemplo:

- Em uma NF-e que possui 500 itens, terá que dividir em 2 documentos com 250 itens cada.
- Caso o erro de tamanho do lote ainda persista, deve-se dividir a quantidade de itens em mais notas.

#### Erro Finalizando documento: Existem Contas de Projeto, que são incompatíveis com o processo X/XXXX !

**Causa:** O motivo do erro ser incompatível com o processo é devido ao processo vinculado a NF é do tipo **Conta Própria** e a **Conta Projeto** que foi herdada está como **Nenhum** ou está diferente do Processo, por exemplo **Conta e Ordem de Terceiros**.

**Solução:** Neste caso, deverá verificar com o responsável pela manutenção deste cadastro, que geralmente é o Setor Contábil/Fiscal para efetuar os devidos ajustes no seguinte menu: Cadastro de Projeto > Aba Contas > Campo Tipo Operação.

#### Mensagem: Esta NF-e está vinculada a um documento que não é NF-e.

**Informações:** A mensagem acima é apenas um aviso gerado pelo Conexos para informar que a NF-e que está sendo transmitida está vinculada a um documento que não é NF-e. Essa mensagem ocorre pois a(s) nota(s) vinculada(s) no botão logística é do tipo própria = não, ou seja, não foi emitida pela filial. De qualquer forma, esta **é apenas uma mensagem de aviso que não impedirá a transmissão da NF-e** e finalização do documento no Conexos.

#### ERRO: REJEIÇÃO IE DO DESTINATARIO NAO ESTÁ ATIVA NA UF, PORÉM, EM CONSULTA AO SINTEGRA O CLIENTE DA NOTA FISCAL ESTÁ ATIVO.

**Causa:** O erro ocorre devido a alguma irregularidade no CNPJ/IE do destinatário.

**Solução:** Entre em contato com seu cliente solicitando que o mesmo verifique com sua contabilidade se há alguma pendência junto a SEFAZ que precise ser regularizada.

#### ERRO: A SÉRIE DESTE DOCUMENTO NAO ESTA CONFIGURADA PARA A NF-E

**Causa:** Este erro ocorre pois não há regime NF-e configurado para a filial 9.

**Solução:** Para solucionar esse problema se deve acessar a tela CMN_136 - regime NFE e proceder com o cadastro.

- Informar validade
- Tipo de NF-e = Regime de transmissão normal.

Em seguida prosseguir com o faturamento.

#### ERRO: ENVIANDO DOCUMENTO PARA HOMOLOGAÇAO: O VALOR TOTAL INFORMADO NO DOCUMENTO É DIFERENTE DO VALOR LIQUIDO CALCULADO.

**Causa:** A causa dos erros é devido ao valor atribuído no campo "VALOR TOTAL DA NOTA FISCAL" na tela Fiscais de Saída e no botão da tela Fiscais de Saída → "MAIS AÇÕES" → "ENCARGOS GERAIS" não constar o mesmo valor.

**Solução:** Para que este erro não ocorra é necessário inserir as mesmas informações no campo "VALOR TOTAL DA NOTA FISCAL" e "ENCARGOS GERAIS" pois o valor líquido é considerado a partir dos itens da NF e quando não há produto vinculado a mensagem aparece.

#### ERRO: A DATA DE MOVIMENTO DA NOTA FISCAL EXCEDEU A TOLERANCIA DE 15 MINUTOS DO MOMENTO DA HOMOLOGAÇAO.

**Causa:** Os erros ocorrem no momento da homologação do documento onde a rotina possui uma trava que não permite transmitir NF-e após 15 minutos entre a Data/Hora de geração até que o documento seja homologado.

**Solução:** Para que este erro não ocorra é necessário limpar os campos "DATA/HORA EMISSÃO" e "DATA/HORA SAÍDA" antes de homologar os documentos. Fiscais de Saída → "MAIS AÇÕES" → "FISCAL" → "QUADRO INFORMAÇÕES NF-E/ROMANEIO" → **"DATA/HORA EMISSÃO" e "DATA/HORA"**

#### Erro: CONTA FINANCEIRA NÃO CONFIGURADA PARA BAIXA A RECEBER. DOCUMENTO XXX

**Causa:** A validação do documento pode estar sendo impactada pela ausência de informações no plano financeiro utilizado, seja no documento ou na filial.

**Solução:** Verifique se o campo **Quitações a Receber** está devidamente preenchido na tela Plano de Contas Financeiro para o plano financeiro em questão.

#### Erro: VALOR BAIXADO MAIOR QUE O DISPONIVEL PARA O TITULO (DOCUMENTO: XXXX). VALOR EM ABERTO: XXXXX VALOR RESERVADO (PEDIDOS): XXXXX

**Causa:** Esse erro ocorre quando há divergência entre o valor de adiantamento disponível na tela COM034 > Mais Ações > Adiantamento e o valor dos pedidos. Isso acontece quando um adiantamento é associado com valor maior do que o devido em um ou mais pedidos, fazendo com que o total reservado ultrapasse o valor disponível.

**Solução:** Acessar o pedido onde o adiantamento foi vinculado incorretamente, cancelar o vínculo e refazê-lo com o valor correto. É importante garantir que a soma dos valores dos pedidos não ultrapasse o valor total do adiantamento disponível.

## Informações Técnicas

Consulte o detalhamento referente a campos, filtros e botões desta tela no Manual Técnico de Geração Automática de NF-e.

## Referência Interna

- Fiscais de Entrada: Origem das notas de entrada (Própria).
- Fiscais de Saída: Origem das notas de saída (Venda/Remessa).
- Cadastro de Séries: Configuração de modelo (55) e layouts de impressão.
- Configuração de Certificados: Armazenamento do certificado digital A1.
- Cadastro de Processos: Fonte de dados (Adquirente) para notas de terceiros.
- Log Tarefas Robô: Tela de diagnóstico técnico profundo (Java/XML).
- Parâmetros da Filial: Define o ambiente de envio (Homologação/Produção).

## Referência Externa

*(Sem conteúdo listado na página no momento da extração.)*
