# Base Erros Conexos

## Base Erros Conexos

#### SPED Contribuições: registros 1010/1011 em branco (exclusão do ICMS da base PIS/COFINS)

- **HD:** 10
- **Tipo:** Erro/Incidente
- **Módulo:** SPED - EFD Contribuições
- **Cliente:** Comexport
- **Data abertura:** 29/10/2019
- **Problema citado:** Ao gerar o SPED Contribuições (mês 10, filial 18) os registros 1010 e 1011 saem em branco.
- **Erro apresentado:** Registros 1010/1011 sem conteúdo no arquivo.
- **Solução proposta pela Conexos:** Para gerar o 1011 (detalhamento do 1010) a nota fiscal precisa ter o encargo de desconto da base PIS/COFINS, configurado no CFOP conforme a necessidade de cálculo. Implementação seguiu escopo aprovado anteriormente.

#### NFS-e sem destaque do ISS 3% (SC)

- **HD:** 18
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Seth
- **Data abertura:** 08/04/2020
- **Problema citado:** NF de serviço (ganho de comissão) emitida manualmente nos Fiscais de Saída (CFOP 5933-A1) não destacou o ISS de 3%.
- **Erro apresentado:** XML gerado com natureza de operação 111 (ISS devido para outro município), sem destaque do ISS.
- **Solução proposta pela Conexos:** A natureza de operação é definida por validações do cadastro da filial e da pessoa (regime de apuração, código IBGE do local de prestação etc.). Ajustar os cadastros para que o local de prestação/apuração gere a natureza correta.

#### Erro no vínculo de DI

- **HD:** 42
- **Tipo:** Erro/Incidente
- **Módulo:** Comex Importação
- **Cliente:** Vequis
- **Data abertura:** 08/12/2022
- **Problema citado:** Erros ao vincular a DI ao processo e dúvida se o cadastro de produtos é acrescido a cada novo vínculo.
- **Erro apresentado:** FCA: valor das despesas declaradas no conhecimento (0,00) não confere com a DI; plano financeiro do exportador/fabricante não encontrado.
- **Solução proposta pela Conexos:** Vincular o CE (conhecimento) ao processo e informar o plano financeiro no cadastro do exportador/fabricante antes de refazer o vínculo da DI.

#### Descrição do produto inconsistente na DANFE

- **HD:** 60
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Savixx
- **Data abertura:** 19/01/2023
- **Problema citado:** Descrição dos produtos sai diferente entre notas de entrada e saída e até entre itens da mesma DANFE (duplicada ou cortada).
- **Erro apresentado:** Descrição do item sem padrão na NF-e.
- **Solução proposta pela Conexos:** O sistema monta a descrição nesta ordem de prioridade: 1) Cadastro de Pessoas (CMN023) > Comercial > Identificação dos itens na NF; 2) ODF (IMP002) > Informações NF-e; depois demais fontes. Padronizar a configuração na fonte que prevalece.

#### Regra contábil de valor 'Crítica processos com remessa para armazenagem' (CTB_007)

- **HD:** 83
- **Tipo:** Dúvida
- **Módulo:** Contabilidade
- **Cliente:** Columbia
- **Data abertura:** 02/12/2025
- **Problema citado:** Dúvida sobre o funcionamento da regra contábil de valor 'Crítica processos com remessa para armazenagem'.
- **Solução proposta pela Conexos:** A regra avalia o documento de entrada com processo vinculado: se o tipo do processo for Conta Própria, contabiliza; caso contrário, não contabiliza.

#### Erro na transmissão de NFS-e (COM303) - certificado e tag EmailTomador

- **HD:** 109
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** G4
- **Data abertura:** 05/09/2024
- **Problema citado:** Emissão de NF de serviço na filial 01 (COM297) falha na transmissão.
- **Erro apresentado:** 'Certificado não encontrado, envie seu certificado digital para continuar emitindo'; depois: 'Para essa cidade o campo referente à tag EMAILTOMADOR é obrigatório e não deve ser maior que 80 caracteres'.
- **Solução proposta pela Conexos:** Conexos ajustou o certificado da filial 1. Para o novo erro, preencher o e-mail do tomador (até 80 caracteres) no cadastro, exigência do município.

#### Tag xLocDesemb (local de desembaraço) no XML

- **HD:** 113
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Vequis
- **Data abertura:** 04/12/2023
- **Problema citado:** Necessidade de definir a origem da informação do local de desembaraço no XML da NF-e.
- **Erro apresentado:** Tag preenchida sempre com a URF de despacho.
- **Solução proposta pela Conexos:** Escopo: novo parâmetro na GER010 'Local desembaraço tag XML' (Recinto / URF Despacho, padrão URF Despacho). Hoje busca a URF despacho da IMP_019 (com DI) ou do conhecimento (LOG_012) sem DI.

#### Balanço Patrimonial e DRE no Conexos

- **HD:** 119
- **Tipo:** Dúvida
- **Módulo:** Contabilidade
- **Cliente:** Nutex
- **Data abertura:** 22/06/2022
- **Problema citado:** Usuário não encontra relatórios de Balanço e DRE, apenas balancetes.
- **Solução proposta pela Conexos:** Configuração do Balanço e DRE na tela FIN006. Relatórios: DMPL RP_CTB_135; Balanço: Plano de Contas Gerencial 1 coluna (RP_COM_048); DRE: Plano de Contas Gerencial 15 colunas (RP_COM_049).

#### Geração da GIA normal e GIA-ST

- **HD:** 146
- **Tipo:** Erro/Incidente
- **Módulo:** Fiscal
- **Cliente:** Comexport
- **Data abertura:** 03/01/2020
- **Problema citado:** GIA-ST da filial 01 não trazia a nota fiscal lançada.
- **Erro apresentado:** Nota não gerada no arquivo da GIA-ST.
- **Solução proposta pela Conexos:** Na tela CTB010, ao gerar o arquivo, informar a UF SP (UF de destino do ST). Assim a nota lançada é gerada no arquivo.

#### Tag uTrib do XML com unidade comercial em vez da estatística

- **HD:** 167
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Vequis
- **Data abertura:** 30/10/2024
- **Problema citado:** Cliente precisa que a tag uTrib traga a unidade estatística (litro) da invoice/NCM, mas o XML traz a unidade comercial.
- **Erro apresentado:** uTrib preenchida com a unidade comercial.
- **Solução proposta pela Conexos:** Na NF gerada via ODF os valores tributários (qtd trib., valor unit. trib., unidade trib.) não estavam preenchidos, então o sistema usa a unidade comercial. Preencher os dados tributários no cadastro do produto/documento conforme a validação de faturamento de ODF.

#### Geração do C197 para DIFAL (uso e consumo/imobilizado)

- **HD:** 172
- **Tipo:** Dúvida
- **Módulo:** Fiscal
- **Cliente:** Power Trade
- **Data abertura:** 13/03/2020
- **Problema citado:** Como gerar o C197 do SPED Fiscal para ajuste de diferencial de alíquotas em aquisições interestaduais.
- **Solução proposta pela Conexos:** Os registros de ajuste de DIFAL são fixos na rotina (ex.: C195 999001 / 999099). Se faltar algum código de ajuste, solicitar inclusão via HD.

#### Variáveis de CFOP com dados completos do armazém

- **HD:** 173
- **Tipo:** Dúvida
- **Módulo:** Fiscal
- **Cliente:** Comexport
- **Data abertura:** 31/01/2020
- **Problema citado:** Necessidade de variável no CFOP para trazer dados do armazém, pois o mesmo CFOP envia para vários armazéns.
- **Solução proposta pela Conexos:** Variáveis disponíveis: #RZS_ARM (razão social do armazém, CMN_025), #IMP_CGC (CNPJ do endereço padrão), #COM_END (logradouro, nº, complemento, bairro, cidade/UF do endereço padrão).

#### C197 com crédito presumido TTD 410 (SC)

- **HD:** 174
- **Tipo:** Erro/Incidente
- **Módulo:** SPED - EFD Fiscal
- **Cliente:** Power Trade
- **Data abertura:** 13/03/2020
- **Problema citado:** Sistema gera apenas os códigos SC54000001 e SC24000001; necessidade de ajuste de outros créditos no C197 nas saídas com crédito presumido do TTD 410.
- **Erro apresentado:** Códigos de ajuste incompletos no C197.
- **Solução proposta pela Conexos:** 1) GER008: configurar 'Classificação industrial ou equiparado' (registro 0002). 2) CTB031: cadastrar os novos códigos de ajuste (C197/E110/E111/1900). 3) CTB009: campo código de ajuste para lançamentos manuais (cancelar e relançar os existentes).

#### 'Período contábil bloqueado' na importação de XML (COM297)

- **HD:** 200
- **Tipo:** Erro/Incidente
- **Módulo:** Contabilidade
- **Cliente:** Columbia
- **Data abertura:** 20/02/2026
- **Problema citado:** Ao importar XML de NFs de armazenagem do ano anterior aparece período contábil bloqueado, embora a contabilidade tenha aberto o período.
- **Erro apresentado:** Mensagem 'Período contábil bloqueado'.
- **Solução proposta pela Conexos:** O Conexos tem camadas adicionais de bloqueio. Validar a liberação de períodos na tela GER_002 e os demais parâmetros globais/operacionais de bloqueio antes de reimportar.

#### Erro no PVA da ECD: mais de uma linha de nível 1 na DRE (J150)

- **HD:** 204
- **Tipo:** Erro/Incidente
- **Módulo:** Contabilidade
- **Cliente:** Power Trade
- **Data abertura:** 30/06/2020
- **Problema citado:** Validação da ECD exige alteração da estrutura da DRE.
- **Erro apresentado:** PVA: 'Não deve existir mais de uma linha de nível igual 1 na DRE'.
- **Solução proposta pela Conexos:** Mudança de leiaute do J150. Corrigir na FIN006 > aba Contas, deixando apenas um nível 1 (totalizador) na DRE.

#### Restringir acesso de usuários por horário

- **HD:** 218
- **Tipo:** Dúvida
- **Módulo:** Administração do sistema
- **Cliente:** Yaha
- **Data abertura:** 20/03/2020
- **Problema citado:** Dúvida se é possível bloquear o acesso de usuários fora de determinado horário.
- **Solução proposta pela Conexos:** Configurar acesso por horário e IP na GER_091 e vincular ao usuário na GER_004 (campo Configurações de acesso). Apenas o usuário administrador pode configurar.

#### NF de entrada com IPI maior que o da DI

- **HD:** 227
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Luxor
- **Data abertura:** 06/07/2022
- **Problema citado:** IPI da NF de entrada do processo 1113 maior que o valor da DI.
- **Erro apresentado:** Divergência de IPI entre NF e DI.
- **Solução proposta pela Conexos:** Parâmetro GER008 'Forma de cálculo do acréscimo' = Realizar rateio se houver gerou problema no THC ao vincular a DI. Revincular a DI com sequência 1, cancelar a ODF e refaturar.

#### Coluna Crédito Presumido do relatório de apuração (RPCTB142) nas devoluções

- **HD:** 306
- **Tipo:** Erro/Incidente
- **Módulo:** Fiscal
- **Cliente:** Comexport
- **Data abertura:** 02/04/2020
- **Problema citado:** Valores de crédito presumido nas devoluções incorretos no relatório de fechamento.
- **Erro apresentado:** Crédito presumido divergente no relatório.
- **Solução proposta pela Conexos:** A coluna não lê o encargo de crédito presumido do documento; calcula % benefício x 0,01 x base ICMS x 0,01 x % máximo do tributo. Ajuste é no relatório, não no documento.

#### Controle de poder de terceiros não funcionando

- **HD:** 309
- **Tipo:** Erro/Incidente
- **Módulo:** Fiscal
- **Cliente:** Comexport
- **Data abertura:** 03/04/2020
- **Problema citado:** Evidência de que o controle de poder de terceiros não funciona (NF 29190).
- **Erro apresentado:** Saldo de terceiros não controlado.
- **Solução proposta pela Conexos:** O controle depende do vínculo correto entre remessa e retorno na COM_091 > aba Doc. Vinculados > Documento Retorno: nas entradas vincular a NF de saída (venda/remessa); nas saídas vincular a NF de entrada (aquisição/devolução).

#### Produto não disponível na NF de remessa (filial 22)

- **HD:** 313
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Comexport
- **Data abertura:** 06/04/2020
- **Problema citado:** Ao emitir NF de remessa para armazenagem o produto 152 não aparece.
- **Erro apresentado:** Produto não localizado ao digitar o código.
- **Solução proposta pela Conexos:** A GER_010 tinha ativo 'Utiliza liberação de produtos', exigindo liberação na COM_039. Trava retirada, pois não há processo de requisição de material.

#### Ajustes no relatório de fechamento fiscal

- **HD:** 316
- **Tipo:** Dúvida
- **Módulo:** Fiscal
- **Cliente:** Comexport
- **Data abertura:** 07/04/2020
- **Problema citado:** Dúvida se as correções do relatório de fechamento foram feitas nos documentos fiscais.
- **Solução proposta pela Conexos:** As alterações foram feitas apenas no relatório. Ele valida entradas/saídas, incentivo, finalização, datas, CFOP, produto, NCM, base, valor e % de ICMS.

#### Erro ao faturar NF de entrada: quantidade diferente das séries vinculadas

- **HD:** 338
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Comexport
- **Data abertura:** 17/04/2020
- **Problema citado:** Faturamento de entrada (IMP002) bloqueado no processo 190712.
- **Erro apresentado:** 'Não é permitido faturar um item com quantidade informada diferente da quantidade de séries vinculados. Ref. adição 2 / item 2'.
- **Solução proposta pela Conexos:** Séries não vinculadas corretamente na DI (aba Mercadorias da IMP002). Refazer o vínculo da DI item a item e refazer a ODF.

#### Instalação de certificado digital e-CPF (Siscoserv)

- **HD:** 361
- **Tipo:** Erro/Incidente
- **Módulo:** Siscoserv
- **Cliente:** Comexport
- **Data abertura:** 30/04/2020
- **Problema citado:** Erro ao instalar certificado e-CPF A1.
- **Erro apresentado:** Erro na importação do certificado na COM324.
- **Solução proposta pela Conexos:** COM_324 é para e-CNPJ (emissão de NF, tipo A1), só pelo usuário gestor. e-CPF vai na GER_078 (DI/LI Siscomex). Siscoserv usa o certificado instalado na máquina do agente integrador.

#### Rejeição 697 em venda interestadual de leasing (alíquota 4%)

- **HD:** 364
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Comexport
- **Data abertura:** 04/05/2020
- **Problema citado:** Faturamento do processo 190720 (venda interestadual a não contribuinte, item CAMEX, redução para 4%) rejeitado.
- **Erro apresentado:** Rejeição 697: alíquota interestadual do ICMS com origem diferente do previsto.
- **Solução proposta pela Conexos:** pICMSInter 4% só é aceito para origens 1, 2, 3 e 8 (importados/conteúdo de importação acima de 40%). Ajustar a origem da mercadoria ou a alíquota interestadual.

#### PIS/COFINS e CIF da NF de entrada divergentes da DI

- **HD:** 370
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Comexport
- **Data abertura:** 06/05/2020
- **Problema citado:** NF de entrada do processo 120293 com PIS/COFINS pela metade do valor da DI e CIF divergente, apesar de o CFOP 3102-K1 buscar valores da DI.
- **Erro apresentado:** Valores de impostos e CIF divergentes da DI.
- **Solução proposta pela Conexos:** Causa na unidade de medida: produto com unidade primária kg líquido e sugestiva tonelada (1.000 kg = 1 t). Conferir quantidade x unidade da invoice e a conversão do cadastro do produto.

#### Origem dos campos 050 e 060 do Quadro 04 da DIME (SC)

- **HD:** 377
- **Tipo:** Dúvida
- **Módulo:** Fiscal
- **Cliente:** Comexport
- **Data abertura:** 08/05/2020
- **Problema citado:** Dúvida sobre a origem dos valores dos campos 050 e 060 do Quadro 04 da DIME (RP_CTB_086).
- **Solução proposta pela Conexos:** Quadro 04 resume a apuração dos débitos. Item 050 (estorno de crédito) vem de benefício fiscal que exige estorno; conferir os encargos/ajustes que alimentam cada item conforme orientação anexada.

#### Divergência no livro de saída (Outras ICMS)

- **HD:** 404
- **Tipo:** Erro/Incidente
- **Módulo:** Fiscal
- **Cliente:** Comexport
- **Data abertura:** 15/05/2020
- **Problema citado:** Valores na coluna Outras do livro de saída divergentes.
- **Erro apresentado:** Livro com valor de IPI na coluna Outras.
- **Solução proposta pela Conexos:** Regra 'Livro fiscal / ICMS / Outras': saída com redução de BC do ICMS retorna o IPI; entrada exonerada retorna valor contábil; BC ou ICMS zero retorna valor contábil. NFs 2083/2088 têm redução de base.

#### Diferenças no livro de entradas (despesas acessórias na coluna IPI)

- **HD:** 412
- **Tipo:** Erro/Incidente
- **Módulo:** Fiscal
- **Cliente:** Comexport
- **Data abertura:** 18/05/2020
- **Problema citado:** Livro de entradas (RP_CTB_003) não considerou despesas acessórias na coluna IPI, entre outros casos.
- **Erro apresentado:** Valores fiscais do IPI divergentes no livro.
- **Solução proposta pela Conexos:** A coluna de IPI segue o parâmetro do CFOP (CMN_023 > Avançado > IPI): se Nenhum/Não incidente/Isento, soma os valores do encargo IPI (GER_047). Ajustar a configuração do CFOP conforme o caso.

#### CST do ICMS em CFOP com ICMS-ST de saída

- **HD:** 430
- **Tipo:** Dúvida
- **Módulo:** Faturamento + NF-e
- **Cliente:** Comexport
- **Data abertura:** 23/05/2020
- **Problema citado:** Dúvida sobre qual CST informar no CFOP com ICMS-ST na saída.
- **Solução proposta pela Conexos:** Configuração do CFOP correta. Preparação de base ST 100% considera o valor total do encargo de origem mais os encargos de detalhe. O CST pode ficar 'Nenhum': o sistema define automaticamente conforme existência de ST e tributação.

#### Cadastro do Fundo de Combate à Pobreza (FCP)

- **HD:** 431
- **Tipo:** Dúvida
- **Módulo:** Faturamento + NF-e
- **Cliente:** Comexport
- **Data abertura:** 23/05/2020
- **Problema citado:** Dúvida sobre como cadastrar os encargos do FCP e configurar os CFOPs.
- **Solução proposta pela Conexos:** 1) CMN005: cadastrar encargos de base do FCP, valor do FCP e base do FCP na UF de destino. 2) GER_047: vincular os encargos aos campos correspondentes. 3) Configurar os CFOPs com os encargos.

#### Série fiscal de NFS-e/RPS por município (Vitória, Cariacica, Itajaí)

- **HD:** 439
- **Tipo:** Dúvida
- **Módulo:** Faturamento + NF-e
- **Cliente:** Comexport
- **Data abertura:** 26/05/2020
- **Problema citado:** Dúvida sobre como cadastrar a série fiscal das notas de serviço em cada filial (NFS-e ou RPS).
- **Solução proposta pela Conexos:** A série depende das regras de cada prefeitura. Itajaí: RPS usam séries RP1, RP2, RP3 em sequência; ao atingir o limite de numeração, reiniciar com nova série.

#### Exclusão de invoice

- **HD:** 440
- **Tipo:** Erro/Incidente
- **Módulo:** Comex Importação
- **Cliente:** Altra
- **Data abertura:** 18/01/2022
- **Problema citado:** Necessidade de excluir invoice (cód. 1618) vinculada a processo.
- **Erro apresentado:** Invoice não pode ser excluída por ter vínculos.
- **Solução proposta pela Conexos:** Antes de excluir, remover o destaque do item (aba Itens > Destaque resumo) e o registro de LI na IMP_095, quando houver. Conexos excluiu as invoices.

#### Faturamento com frete maior que o FOB (valor líquido negativo na invoice)

- **HD:** 443
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Columbia
- **Data abertura:** 12/06/2026
- **Problema citado:** Faturamento de processo em que o frete é maior que o FOB.
- **Erro apresentado:** Invoice com Valor Líquido negativo em todos os itens.
- **Solução proposta pela Conexos:** 1) Excluir a ODF; 2) cancelar a SP de impostos na IMP_223; 3) excluir a Duimp; 4) na invoice (LOG_009) alterar o 'rateio do peso' para FOB e seguir a ordem de ajustes indicada; refazer o processo.

#### Erro ao gerar XML de ND de baixa de estoque (perda)

- **HD:** 489
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Columbia
- **Data abertura:** 16/07/2026
- **Problema citado:** Nota de débito do tipo perda em estoque não gera XML (filial 2, doc. 728).
- **Erro apresentado:** 'ERRO GERANDO XML: GERANDO PISOUTR Q05 - PISPPIS'.
- **Solução proposta pela Conexos:** Os encargos de PIS e COFINS não estavam no CFOP/documento (COM_297 > Itens > Encargos). Incluir os encargos no CFOP e reprocessar.

#### Trava GER_008 'Validar IBS/CBS'

- **HD:** 502
- **Tipo:** Dúvida
- **Módulo:** Faturamento + NF-e
- **Cliente:** Columbia
- **Data abertura:** 22/07/2026
- **Problema citado:** Dúvida sobre o funcionamento da trava de validação de IBS/CBS na ODF e no pedido de venda.
- **Solução proposta pela Conexos:** GER_008 > Faturamento > 'Validar IBS/CBS'. Não = sem validação. Sim = valida se há CST de IBS/CBS no CFOP (CMN023 > SPED/NF-e > IBS-CBS-IS) usado na IMP_002/COM_034 e se os encargos de IBS/CBS estão presentes.

#### Faturamento bloqueado: custo médio entre processos / unidade do produto

- **HD:** 523
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Columbia
- **Data abertura:** 04/08/2026
- **Problema citado:** Processo 3278 (filial 2) não fatura mesmo após quebrar em 5 notas e mudar a unidade para tonelada.
- **Erro apresentado:** Sistema calculando custo médio incorreto entre processos.
- **Solução proposta pela Conexos:** Causa: campo 'Qtd embalagem' das unidades kg líquido e tonelada (COM_006 > produto 2652 > Unidades) alterado repetidamente entre 1 e 1.000. Corrigir a equivalência das unidades e não alterá-la com movimentações em aberto.

#### Importação do extrato bancário a cada hora e risco de duplicidade

- **HD:** 525
- **Tipo:** Dúvida
- **Módulo:** Financeiro
- **Cliente:** Columbia
- **Data abertura:** 04/08/2026
- **Problema citado:** Dúvida se importar o extrato a cada hora gera lançamentos duplicados.
- **Solução proposta pela Conexos:** Já existe validação: lançamentos com mesmo valor e mesma data são classificados como 'Duplicado' e marcados para 'Não importar'.

#### DI registrada antes do Conexos sem XML para download (IMP_188)

- **HD:** 526
- **Tipo:** Erro/Incidente
- **Módulo:** Comex Importação
- **Cliente:** Columbia
- **Data abertura:** 04/08/2026
- **Problema citado:** Para fiscalização, consulta de DIs desde 01/2022 pelo robô traz muitas DIs sem XML.
- **Erro apresentado:** XML da DI não disponível.
- **Solução proposta pela Conexos:** As DIs não estavam consultadas. Selecionar a DI e clicar em 'Consulta web' para baixar o XML. Não consultar muitos registros ao mesmo tempo.

#### Inutilização de numeração de NF-e

- **HD:** 537
- **Tipo:** Erro/Incidente
- **Módulo:** Fiscal
- **Cliente:** Comexport
- **Data abertura:** 16/06/2020
- **Problema citado:** NF de entrada nº 82 (série NFE4, filial 3) não foi inutilizada.
- **Erro apresentado:** Numeração não inutilizada na SEFAZ.
- **Solução proposta pela Conexos:** A inutilização automática não inutiliza notas canceladas; só números não enviados dentro de uma sequência existente. Como houve cancelamento sem transmissão, inutilizar manualmente.

#### Erro de schema na transmissão: UF 'EX' (encomendante do exterior)

- **HD:** 539
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Columbia
- **Data abertura:** 11/08/2026
- **Problema citado:** NF de entrada do processo 622 (filial 6) não transmite, apesar de o fornecedor estar correto.
- **Erro apresentado:** 'cvc-enumeration-valid: Value EX is not facet-valid with respect to enumeration [AC, AL, ... TO]'.
- **Solução proposta pela Conexos:** Na IMP021, quadro Encomendante/Adquirente, foi informada pessoa do exterior. Informar o encomendante/adquirente nacional correto.

#### API de logout retorna 200 mas não encerra a sessão

- **HD:** 543
- **Tipo:** Erro/Incidente
- **Módulo:** DBA + Infra
- **Cliente:** Savixx
- **Data abertura:** 28/08/2025
- **Problema citado:** Integrações via API: logout retorna 200 OK mas a sessão continua contando.
- **Erro apresentado:** Limite de sessões atingido.
- **Solução proposta pela Conexos:** A API segue o mesmo limite do sistema (máximo 4 logins). Sessões abertas no sistema e na API somam; encerrar sessões abertas no sistema.

#### Cancelar e-mails antigos pendentes de envio (homologação)

- **HD:** 547
- **Tipo:** Dúvida
- **Módulo:** DBA + Infra
- **Cliente:** Columbia
- **Data abertura:** 24/08/2026
- **Problema citado:** Necessidade de cancelar e-mails antigos que seriam enviados pelo ambiente de homologação.
- **Solução proposta pela Conexos:** Rotina automática limpa os logs da GER_009: e-mails 'Enviado' com mais de 10 dias e 'Erro' com mais de 30 dias são apagados.

#### NF transmitida não finaliza por divergência no lote contábil

- **HD:** 567
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Columbia
- **Data abertura:** 02/09/2026
- **Problema citado:** Após transmitir à SEFAZ, o documento não finaliza; é preciso rodar o PRS_011 para corrigir o custo.
- **Erro apresentado:** Divergência no lote contábil ao finalizar.
- **Solução proposta pela Conexos:** COFINS e COFINS Custo buscam o classificador de produtos 1 (COFINS majoração), configurado com 'Ação sobre o custo = Nenhum'. Ajustar o classificador para tratar corretamente o custo.

#### Geração do Bloco K220 no SPED Fiscal

- **HD:** 588
- **Tipo:** Dúvida
- **Módulo:** SPED - EFD Fiscal
- **Cliente:** Comexport
- **Data abertura:** 26/06/2020
- **Problema citado:** Comexport entende que devem ser entregues o 0205 e o K220 na mudança de código de produto.
- **Solução proposta pela Conexos:** K220 é para movimentações internas entre mercadorias; mudança de código não é movimentação. Gerar K220 só nas duas hipóteses do Guia Prático (reclassificação por destinatário, etc.).

#### Erro ao gerar NF de entrada com lotes: tag dVal

- **HD:** 600
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Capital Trade
- **Data abertura:** 06/04/2020
- **Problema citado:** Faturista não consegue gerar NF de entrada de produtos com lote.
- **Erro apresentado:** Erro na geração do XML na tag dVal (data de validade).
- **Solução proposta pela Conexos:** Produtos com data de validade do lote em formato inválido. Corrigir em COM_006 > botão Lotes.

#### Rejeição E0120 na NFS-e nacional (RJ): IM do prestador

- **HD:** 609
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Savixx
- **Data abertura:** 06/01/2026
- **Problema citado:** Emissão de NFS-e no RJ (filial 10) rejeitada.
- **Erro apresentado:** E0120: 'IM do prestador não deve ser informado, pois não existem informações complementares registradas no CNC NFS-e do município emissor'.
- **Solução proposta pela Conexos:** Remover a inscrição municipal na GER_007 antes de processar o documento.

#### DIME de junho com Declaração Complementar Anual (quadros 80 a 84)

- **HD:** 612
- **Tipo:** Dúvida
- **Módulo:** Fiscal
- **Cliente:** Comexport
- **Data abertura:** 02/07/2020
- **Problema citado:** Como gerar a DIME de junho com as informações contábeis anuais.
- **Solução proposta pela Conexos:** Já fixo na rotina: quadros 80 a 84 vêm do balancete RP_CTB_007. Ver tópicos 4 e 5 do manual da DIME na Wiki.

#### THC incorreto na NF de entrada

- **HD:** 620
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Capital Trade
- **Data abertura:** 05/05/2020
- **Problema citado:** NF de entrada do processo 58757 com THC de 6.420,63 quando o correto (soma das adições) é 710,00.
- **Erro apresentado:** THC divergente da DI.
- **Solução proposta pela Conexos:** Pesos dos itens divergentes dos pesos das adições (DI não registrada pelo Conexos). Corrigir pesos na invoice e executar o procedimento de atualizar pesos da DI.

#### Ajuste da base de cálculo do ICMS na importação

- **HD:** 638
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Capital Trade
- **Data abertura:** 01/06/2020
- **Problema citado:** Após ajustar o valor do produto, a base de ICMS também mudou e não bate com o valor esperado.
- **Erro apresentado:** Base de ICMS incorreta.
- **Solução proposta pela Conexos:** Incluir o encargo de preparação de base no CFOP com todos os impostos da composição (botão Detalhes) e configurar o encargo de base do ICMS para incidir sobre a preparação de base aplicando o fator.

#### Máscara de referência do processo por modalidade (encomenda)

- **HD:** 651
- **Tipo:** Dúvida
- **Módulo:** Comex Importação
- **Cliente:** Capital Trade
- **Data abertura:** 02/07/2020
- **Problema citado:** Criar sequência de referência de processo separada por modalidade (ex.: ECTxxxxx/xx).
- **Solução proposta pela Conexos:** Usar a variável #OP na máscara (ex.: #OP-CT#00000/#AA), que retorna sigla conforme finalidade/tipo: EX exportação, EA entreposto, OP conta própria, OC encomenda etc. Ver Wiki 'Máscara do processo'.

#### Rejeições 817 e 388 na NF de exportação

- **HD:** 652
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Capital Trade
- **Data abertura:** 06/07/2020
- **Problema citado:** Falha na transmissão de NF de exportação (COM297).
- **Erro apresentado:** Rejeição 817 (unidade tributável incompatível com o NCM em comércio exterior); depois rejeição 388.
- **Solução proposta pela Conexos:** Sigla da unidade tributável estava incorreta; ajustada para 'KG'. Em seguida tratar a rejeição 388 (código de situação tributária) conforme orientação.

#### Gerar uma NF de saída por container

- **HD:** 666
- **Tipo:** Dúvida
- **Módulo:** Faturamento + NF-e
- **Cliente:** Capital Trade
- **Data abertura:** 21/07/2020
- **Problema citado:** Necessidade de emitir uma nota por container de forma mais ágil.
- **Solução proposta pela Conexos:** IMP002 > Geração automática > opção agrupar NF por container. Na invoice, aba Itens > botão Containers, informar a quantidade por container; o visto passa a separar as ODFs por container.

#### Remessa SISPAG Bradesco com CNPJ diferente do boleto

- **HD:** 681
- **Tipo:** Erro/Incidente
- **Módulo:** Financeiro
- **Cliente:** Yaha
- **Data abertura:** 25/08/2026
- **Problema citado:** Remessas rejeitadas pelo banco por divergência de CNPJ.
- **Erro apresentado:** CNPJ do documento financeiro diferente do boleto.
- **Solução proposta pela Conexos:** Gerar o documento financeiro com o CNPJ do boleto. Não há bloqueio no sistema; uma funcionalidade para informar o CNPJ do boleto exige abertura de HD de melhoria.

#### Rejeição 630 na NF de estorno

- **HD:** 683
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Capital Trade
- **Data abertura:** 18/08/2020
- **Problema citado:** SEFAZ rejeita NF de estorno (doc. 306038, filial 1).
- **Erro apresentado:** Rejeição 630: valor do produto difere do produto valor unitário de tributação x quantidade tributável.
- **Solução proposta pela Conexos:** Ajustar quantidade e valor unitário tributáveis para que o produto seja igual ao valor do item. Caso documentado na Wiki.

#### 'O campo Tributação do IPI (CST) não pode ser nulo' na NF de ajuste

- **HD:** 684
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Comexport
- **Data abertura:** 10/07/2020
- **Problema citado:** NF de ajuste (PRS_025) da NF 314 de remessa para armazenagem falha, mesmo com CST de IPI na nota.
- **Erro apresentado:** 'O campo Tributação do IPI (CST) não pode ser nulo'.
- **Solução proposta pela Conexos:** A regra só considera IPI se valor > 0, CST em 01/02/03/04/49/51-55/99, ou CFOP iniciado em 3 (exceto 3201, 3202, 3211, 3503, 3553). O CST era 05; ajustar o parâmetro correspondente na GER_008 (quadro Nota).

#### Rejeição 611 - cEAN inválido

- **HD:** 698
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Capital Trade
- **Data abertura:** 11/09/2020
- **Problema citado:** Item 550203 não gera nota fiscal.
- **Erro apresentado:** Rejeição 611: cEAN inválido [nItem:3].
- **Solução proposta pela Conexos:** Corrigir o código de barras no cadastro do produto (aba Unidades, coluna Código de barras). O GTIN informado estava inválido.

#### FOB do faturamento divergente da invoice/Duimp (cobertura cambial)

- **HD:** 724
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Savixx
- **Data abertura:** 22/07/2026
- **Problema citado:** FOB do faturamento de saída 91.000 em vez de 91.030 (entrada saiu correta).
- **Erro apresentado:** Valor FOB divergente.
- **Solução proposta pela Conexos:** Produto 34806 com 'Sem cobertura' na IMP_223 (Dados cambiais) e ODF (IMP_002 > Tratamento de exceções) com Cobertura cambial = DI. Alinhar a cobertura cambial entre Duimp e ODF.

#### Faturamento sem data de desembaraço

- **HD:** 731
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Savixx
- **Data abertura:** 07/08/2026
- **Problema citado:** Faturamento precisa sair sem data de desembaraço (processo SA0295-26).
- **Erro apresentado:** Campo data de desembaraço obrigatório.
- **Solução proposta pela Conexos:** Não é possível faturar sem a data. Executar o procedimento PRS179 (Incluir/Alterar data de desembaraço/registro Duimp).

#### Conta financeira na baixa de títulos gerados pela Duimp

- **HD:** 739
- **Tipo:** Erro/Incidente
- **Módulo:** Financeiro
- **Cliente:** Savixx
- **Data abertura:** 18/08/2026
- **Problema citado:** Títulos de impostos da Duimp baixados em conta financeira errada.
- **Erro apresentado:** Baixa na conta 392.
- **Solução proposta pela Conexos:** Ajuste no sistema: passa a considerar primeiro a conta bancária configurada na FIN_005 como conta corrente. O caso ocorreu porque dois planos financeiros tinham os mesmos dados bancários do Pucomex.

#### Vínculo da Duimp: despesas do conhecimento não conferem

- **HD:** 750
- **Tipo:** Erro/Incidente
- **Módulo:** Comex Importação
- **Cliente:** Savixx
- **Data abertura:** 10/09/2026
- **Problema citado:** Duimp não vinculada automaticamente; ao vincular manualmente dá erro.
- **Erro apresentado:** 'CIF - O valor das despesas declaradas no conhecimento (0,00) não confere com a Duimp (140,04)'.
- **Solução proposta pela Conexos:** Para Duimp, as despesas de transporte devem estar configuradas para somar ao frete (exceto THD) na LOG_004 (Tipos de despesas de transporte). Após o ajuste, consultar a Duimp novamente.

#### Baixa de título que estava em remessa SISPAG não paga

- **HD:** 752
- **Tipo:** Erro/Incidente
- **Módulo:** Financeiro
- **Cliente:** Savixx
- **Data abertura:** 17/09/2026
- **Problema citado:** Título da remessa SISPAG não foi pago pelo Bradesco e foi pago por outro banco; baixa bloqueada.
- **Erro apresentado:** 'Este borderô está em um lote...' ao tentar baixar por outro banco.
- **Solução proposta pela Conexos:** Executar o procedimento PRS_040 (Remover título do PAGFOR), informando banco, lote e código do documento. Se não aparecer no menu, usar 'Mostrar todos' e pedir liberação de acesso.

#### DIFAL com encargos negativos quando a base é reduzida

- **HD:** 884
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Comexport
- **Data abertura:** 13/08/2020
- **Problema citado:** Valor do DIFAL divergente e encargos negativos (ex.: T-PICMSUFDEST) em operação com redução de base.
- **Erro apresentado:** Encargos de partilha com valores negativos.
- **Solução proposta pela Conexos:** Configuração de incidência: 'T-AUX_ICMS_PARTILHA' incidia sobre 'T-VBCUFDEST' a 8,8% subtraindo 'T-PICMSINTER', e 'T-PICMSINTERPART' incidia 100%. Revisar as incidências dos encargos de partilha no CFOP.

#### PIS/COFINS destacados na NF filhote de remessa (leasing)

- **HD:** 885
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Comexport
- **Data abertura:** 14/08/2020
- **Problema citado:** Na NF filhote (CFOP 6949-T2) não deve haver destaque de impostos, mas PIS/COFINS aparecem.
- **Erro apresentado:** PIS/COFINS destacados na DANFE.
- **Solução proposta pela Conexos:** As alíquotas de PIS/COFINS só compõem o fator. Apagar a incidência desses encargos ou criar encargos específicos 'Fator p/ PIS' e 'Fator p/ COFINS' para compor o fator sem cálculo.

#### Rejeição 930: CST com benefício fiscal sem cBenef

- **HD:** 944
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Comexport
- **Data abertura:** 26/08/2020
- **Problema citado:** Operação com redução de base (filial 22) exige a tag cBenef; mesmo cadastrado na CMN183 a tag não é preenchida.
- **Erro apresentado:** Rejeição 930: CST com benefício fiscal e não informado o código de benefício.
- **Solução proposta pela Conexos:** O cBenef é enviado conforme o CST e as particularidades da UF. Revisar o cadastro na CMN183 (vínculo CST x UF x código) seguindo as considerações da Conexos.

#### THC não reconhecido ao vincular a DI (incoterm FOB)

- **HD:** 1008
- **Tipo:** Erro/Incidente
- **Módulo:** Comex Importação
- **Cliente:** Capital Trade
- **Data abertura:** 17/11/2021
- **Problema citado:** Processo de Rondônia: conhecimento com THC preenchido, mas o vínculo da DI dá erro.
- **Erro apresentado:** Erro de despesa THC no vínculo da DI.
- **Solução proposta pela Conexos:** Na LOG_004, a despesa THC não tinha configuração para a filial 5 com incoterm FOB. Parametrizar e refazer o vínculo.

#### Como classificar o produto ao abrir HD

- **HD:** 1059
- **Tipo:** Dúvida
- **Módulo:** Administração do sistema
- **Cliente:** Capital Trade
- **Data abertura:** 10/02/2022
- **Problema citado:** Pedido de manual para escolher o produto correto ao abrir HD.
- **Solução proposta pela Conexos:** Não há manual completo. Exemplo: Faturamento = IMP002, COM297, COM296 (própria = sim), COM319/313/327/321/246; os HDs são reclassificados na triagem.

#### Geração automática de ODF por modalidade / validação de tipo de processo por pessoa

- **HD:** 1060
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Capital Trade
- **Data abertura:** 10/02/2022
- **Problema citado:** Dúvida se é possível habilitar a geração automática de ODF só para conta e ordem; erro ao abrir processo.
- **Erro apresentado:** Erro de validação ao salvar o processo.
- **Solução proposta pela Conexos:** Antes de salvar, o sistema valida o tipo de processo por pessoa se GER010 > Processo > 'Valida tipo de processo por pessoa' = Sim (comportamento descrito na Wiki). Ajustar o cadastro da pessoa ou o parâmetro.

#### Rejeição 306: IE do destinatário não ativa

- **HD:** 1145
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Capital Trade
- **Data abertura:** 28/06/2022
- **Problema citado:** Nota de saída não finaliza; Sintegra mostra IE ativa.
- **Erro apresentado:** Rejeição 306: IE do destinatário não está ativa na UF.
- **Solução proposta pela Conexos:** Rejeição da SEFAZ, não do Conexos (documentada na Wiki da COM_319). Confirmar a situação cadastral do destinatário no cadastro da SEFAZ (CCC) e aguardar atualização ou corrigir a IE.

#### Rejeição na NF de estorno: total difere do somatório

- **HD:** 1190
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Capital Trade
- **Data abertura:** 31/08/2022
- **Problema citado:** NF de estorno não é gerada mesmo seguindo procedimento do HD 1189.
- **Erro apresentado:** Rejeição: total da NF difere do somatório dos valores que compõem o total.
- **Solução proposta pela Conexos:** Pelo RP_COM_498 a diferença (R$ 2.846,86) era PIS + COFINS do documento de entrada estornado. Ajustar os encargos de PIS/COFINS no estorno para que componham o total corretamente.

#### Erro de schema na NF complementar de ICMS (pPIS)

- **HD:** 1215
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Capital Trade
- **Data abertura:** 20/10/2022
- **Problema citado:** Não consegue emitir NF complementar de ICMS da nota de entrada.
- **Erro apresentado:** 'cvc-complex-type.2.4.a: Invalid content ... pPIS. One of vBC, qBCProd is expected'.
- **Solução proposta pela Conexos:** O sistema calculava PIS/COFINS por haver alíquotas, mas sem base. Remover/zerar os encargos de PIS/COFINS no CFOP da complementar de ICMS.

#### Descrição do produto na NF após atualização (novos campos)

- **HD:** 1223
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Capital Trade
- **Data abertura:** 07/11/2022
- **Problema citado:** Após atualização, descrição não sai como antes nos Fiscais de Saída.
- **Erro apresentado:** Descrição do item diferente do padrão antigo.
- **Solução proposta pela Conexos:** A rotina não mudou; foram criados novos campos (padrão = 'Padrão'). A validação principal continua na GER008; não é preciso alterar pessoa ou ODF.

#### Processo com itens com e sem TTD 410 (ICMS não calculado)

- **HD:** 1248
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Comexport
- **Data abertura:** 10/11/2020
- **Problema citado:** Processo com itens com e sem benefício TTD 410: ao agrupar por restrição do benefício o ICMS não é calculado.
- **Erro apresentado:** ICMS não calculado no documento.
- **Solução proposta pela Conexos:** Na ODF, Tratamento de exceções > 'ICMS exonerado' = Sim, herdado da configuração de ODF (IMP_047) 'Entrada encomenda - TTD 410'. Ajustar a configuração/ODF para os itens sem benefício.

#### Produtos do inventário fora do Bloco K

- **HD:** 1288
- **Tipo:** Erro/Incidente
- **Módulo:** SPED - EFD Fiscal
- **Cliente:** Comexport
- **Data abertura:** 18/11/2020
- **Problema citado:** Produtos do inventário (ex.: 2837) não aparecem no Bloco K.
- **Erro apresentado:** Itens ausentes no Bloco K.
- **Solução proposta pela Conexos:** Bloco K é gerado se Parâmetros por filial > SPED > 'Envio do bloco K' = Sim, quando enviado o inventário (Bloco H) ou em industrialização com itens vinculados em Notas fiscais - Logística / Itens. Revisar parâmetros e vínculos.

#### Valor da NF de saída divergente quando há redução (encargo Redução de DI)

- **HD:** 1576
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Capital Trade
- **Data abertura:** 19/01/2024
- **Problema citado:** Valor da NF de saída não confere quando há redução.
- **Erro apresentado:** Redução aplicada em duplicidade.
- **Solução proposta pela Conexos:** O encargo 'Redução de DI' estava com 'Ratear valor mercadoria' = Sim, mas a rotina já subtrai a redução do produto. Alterado para Não.

#### NF filhote com valor maior que a NF mãe

- **HD:** 1625
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Capital Trade
- **Data abertura:** 27/02/2024
- **Problema citado:** NF filhote não finaliza alegando valor divergente da mãe.
- **Erro apresentado:** 'O valor total da nota fiscal filhote está maior que a nota fiscal mãe' (mãe 475.225,03 / filhote 950.449,71).
- **Solução proposta pela Conexos:** Validação de homologação da COM297: o total da filhote não pode exceder o da mãe. Corrigir valores/quantidades da filhote (valor estava em dobro).

#### Rejeição por desconto incondicional com regra em looping

- **HD:** 1695
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Capital Trade
- **Data abertura:** 07/05/2024
- **Problema citado:** NF com desconto incondicional vinculado a regra em looping é rejeitada pelo valor do desconto.
- **Erro apresentado:** Rejeição no valor do desconto.
- **Solução proposta pela Conexos:** Cálculo em looping correto (alíquota cadastrada 0,272% x 0,27% da planilha). A rejeição ocorre porque o desconto está sendo destacado; configurá-lo para subtrair no total.

#### Alterar valor/vencimento de títulos já enviados em remessa de cobrança

- **HD:** 1774
- **Tipo:** Melhoria
- **Módulo:** Financeiro
- **Cliente:** Timbro
- **Data abertura:** 13/07/2022
- **Problema citado:** Pedido de implementação para alterar valor e vencimento de títulos já remetidos aos bancos.
- **Solução proposta pela Conexos:** Usar o botão Renegociação na FIN_085, escolhendo o serviço (ex.: alteração de vencimento), a negociação e o leiaute para enviar a instrução ao banco.

#### Valor da NF complementar menor que a despesa (casas decimais)

- **HD:** 1870
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Timbro
- **Data abertura:** 10/10/2022
- **Problema citado:** NF complementar calculando R$ 1.988,98 em vez de R$ 2.120,00.
- **Erro apresentado:** Total e bases menores que a despesa lançada.
- **Solução proposta pela Conexos:** A ODF estava limitada a duas casas decimais. Remover a limitação e refaturar (sobra diferença de centavos por arredondamento do valor do produto).

#### Robô de importação de extratos Nexxera com erro de comunicação

- **HD:** 2125
- **Tipo:** Erro/Incidente
- **Módulo:** Financeiro
- **Cliente:** Level
- **Data abertura:** 04/12/2025
- **Problema citado:** Robô 42 (GER076) de importação de extratos Nexxera falha com frequência.
- **Erro apresentado:** 'WebServiceException: Could not send message'.
- **Solução proposta pela Conexos:** Instabilidade momentânea do webservice; normalmente se resolve sozinha. Se for recorrente, reabrir para análise detalhada.

#### Grupo origComb (UF de origem do combustível) no XML

- **HD:** 2213
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Capital Trade
- **Data abertura:** 29/08/2025
- **Problema citado:** Como evitar novamente o erro na emissão de NF de combustível.
- **Erro apresentado:** Grupo origComb ausente/incorreto.
- **Solução proposta pela Conexos:** Faltava quantidade tributável no cadastro do produto e a rotina só gerava origComb para NCM iniciada em 27. Conexos ajustou a rotina; manter a quantidade tributável preenchida.

#### SPED Fiscal sem o registro 1601

- **HD:** 2215
- **Tipo:** Erro/Incidente
- **Módulo:** SPED - EFD Fiscal
- **Cliente:** Timbro
- **Data abertura:** 17/07/2023
- **Problema citado:** SPED Fiscal (leiaute 17) não gera o registro 1601, obrigatório desde 01/2023.
- **Erro apresentado:** Registro 1601 ausente.
- **Solução proposta pela Conexos:** O 1601 é obrigatório só em algumas UFs. Foi criado campo na CTB048 para o usuário selecionar se o registro será informado.

#### 'Nenhum lote ativo foi encontrado para vincular ao produto'

- **HD:** 2234
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Comexport
- **Data abertura:** 02/07/2021
- **Problema citado:** Faturamento de armazenagem do processo 136050 bloqueado.
- **Erro apresentado:** 'Faturamento da ODF 2 ... nenhum lote ativo foi encontrado para vincular ao produto'.
- **Solução proposta pela Conexos:** Vincular os lotes aos itens na invoice; o sistema usa esse vínculo para vincular automaticamente na saída. Depois faturar a ODF.

#### Emissão de NF e SPED com código de produto do cliente (código externo)

- **HD:** 2313
- **Tipo:** Melhoria
- **Módulo:** Fiscal
- **Cliente:** Comexport
- **Data abertura:** 20/07/2021
- **Problema citado:** Implementação para usar código do produto do cliente na NF-e e reflexos no SPED.
- **Solução proposta pela Conexos:** Conexos pediu definições antes de seguir: se o código do produto (COM006) passaria a ser alfanumérico, tratamento dos produtos antigos e forma de preenchimento.

#### Parametrização de venda com ICMS monofásico (combustíveis)

- **HD:** 2331
- **Tipo:** Dúvida
- **Módulo:** Faturamento + NF-e
- **Cliente:** Capital Trade
- **Data abertura:** 01/12/2025
- **Problema citado:** Pedido de manual para operações com ICMS monofásico.
- **Solução proposta pela Conexos:** Preencher os encargos na GER_047 > quadro 'Operação monofásica - ICMS' (CST 02: BC ICMS tributado e valor ICMS próprio) e no produto alterar 'Detalhamento específico NF-e' para 'Combustíveis'.

#### PTAX incorreta no vínculo da DI (filial 05)

- **HD:** 2334
- **Tipo:** Erro/Incidente
- **Módulo:** Comex Importação
- **Cliente:** Capital Trade
- **Data abertura:** 03/12/2025
- **Problema citado:** Taxa de câmbio incorreta ao vincular DI do processo 1531.
- **Erro apresentado:** Taxa do dólar divergente.
- **Solução proposta pela Conexos:** Na GER008 > Gerais > Moeda, o campo 'Dólar' da filial 5 estava 'Real/Brasil'. Alterado para 'Dólar dos EUA' e refeito o vínculo.

#### Grupo K (medicamentos) da NF-e

- **HD:** 2344
- **Tipo:** Melhoria
- **Módulo:** Fiscal
- **Cliente:** Comexport
- **Data abertura:** 27/07/2021
- **Problema citado:** Implementação do grupo K de medicamentos (código Anvisa) conforme MOC 7.0 / NT 2016.002.
- **Solução proposta pela Conexos:** Conexos pediu detalhes: como identificar que o produto é medicamento e em qual campo/tela ficará a informação.

#### Preenchimento automático do CEST no cadastro de produtos

- **HD:** 2545
- **Tipo:** Dúvida
- **Módulo:** Fiscal
- **Cliente:** Comexport
- **Data abertura:** 16/09/2021
- **Problema citado:** Em quais situações o sistema preenche o CEST automaticamente.
- **Solução proposta pela Conexos:** Tabela CEST atualizada até o Convênio ICMS 52/2017. Ao informar a NCM no produto, o sistema consulta se há CEST equivalente e preenche conforme as situações descritas.

#### DIR de Itajaí: geração e filtro de notas

- **HD:** 2699
- **Tipo:** Dúvida
- **Módulo:** Fiscal
- **Cliente:** Comexport
- **Data abertura:** 04/11/2021
- **Problema citado:** Dúvida se o sistema filtra as notas de Itajaí para Itajaí na DIR.
- **Solução proposta pela Conexos:** Na COM296 deve-se primeiro clicar em 'Gerar lote'; o sistema aplica suas validações para selecionar os documentos da DIR.

#### Divergência de valores no faturamento (base ICMS/IPI)

- **HD:** 2720
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Comexport
- **Data abertura:** 10/11/2021
- **Problema citado:** Valores de produto, BC ICMS e BC IPI divergentes dos esperados.
- **Erro apresentado:** Bases de ICMS e IPI incorretas.
- **Solução proposta pela Conexos:** Incluir encargo de preparação de base do ICMS com os encargos no botão Detalhes; base do ICMS incidindo sobre a preparação com a ordem do IPI na coluna Somar; preparação aplicando fator 1.

#### Faturamento liberado sem estoque (ficha negativa)

- **HD:** 2731
- **Tipo:** Erro/Incidente
- **Módulo:** Estoque
- **Cliente:** Comexport
- **Data abertura:** 12/11/2021
- **Problema citado:** Sistema faturou sem estoque apesar dos bloqueios na GER008.
- **Erro apresentado:** Ficha de estoque negativa.
- **Solução proposta pela Conexos:** Parâmetro da filial 'Controla estoque' = 'Exceto conta própria': o sistema não valida movimentações de processos conta própria. Ajustar o parâmetro se quiser bloquear.

#### Base de cálculo do ICMS divergente do valor dos produtos (valor unitário informado na ODF)

- **HD:** 2761
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Comexport
- **Data abertura:** 23/11/2021
- **Problema citado:** Complemento do HD 2432: NF-e 34376 emitida com o CFOP orientado e a BC do ICMS continua diferente do valor dos produtos.
- **Erro apresentado:** BC ICMS diferente do valor dos produtos.
- **Solução proposta pela Conexos:** Ao informar o valor unitário na aba Mercadorias da ODF, o sistema ignora os encargos de ratear no valor da mercadoria, calcula unitário x quantidade e soma só os encargos de somar. Não informar o valor unitário manualmente quando houver encargos de rateio.

#### Procedimento de NF complementar de quantidade

- **HD:** 2820
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Comexport
- **Data abertura:** 13/12/2021
- **Problema citado:** Confirmação da sequência para gerar complementar de quantidade.
- **Erro apresentado:** Erro ao gerar complementar de quantidade.
- **Solução proposta pela Conexos:** Sequência confirmada: lançar a despesa no processo, gerar a ODF, excluir itens que não serão complementados, fazer a abrangência de rateio indicando a ODF e, na COM_296, marcar 'Complementar de quantidade' = Sim (só quando complementar quantidade; para valor, manter Não).

#### IPI não incluído na base do ICMS em CFOP com exclusão do ICMS da base PIS/COFINS

- **HD:** 2851
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Comexport
- **Data abertura:** 22/12/2021
- **Problema citado:** Faturamento do processo 135169 (filial 3) não inclui IPI na base do ICMS.
- **Erro apresentado:** Fator calculado incorretamente.
- **Solução proposta pela Conexos:** Problema na configuração da exclusão da base. Reconfigurar conforme passo a passo da Conexos, atentando para a posição (ordem) dos encargos, que afeta o cálculo.

#### IE do substituto não aparece na DANFE (DIFAL EC 87/2015)

- **HD:** 2945
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Comexport
- **Data abertura:** 28/01/2022
- **Problema citado:** NF-e 7706 com DIFAL deveria trazer a IE de substituto da UF de destino.
- **Erro apresentado:** IE do substituto ausente na DANFE/XML.
- **Solução proposta pela Conexos:** A IE só é gerada se: a NF tiver ICMS substituído > 0 ou 'ICMS interestadual provisório de partilha'; o encargo ICMS substituto tiver Crédito tributário = Sim; e o CFOP estiver como resultado fiscal, entre outras validações. Ajustar o CFOP/encargos.

#### NF-e complementar x NF-e comum na correção de custo médio

- **HD:** 3011
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Comexport
- **Data abertura:** 17/02/2022
- **Problema citado:** Pedido de embasamento para emitir NF-e comum em vez de complementar.
- **Erro apresentado:** Item sem custo médio.
- **Solução proposta pela Conexos:** Complementar só quando a original precisa de correção/complementação e não cabe devolução/cancelamento: exportação, regularização de preço ou quantidade, lançamento ou correção de impostos. Fora disso, NF comum.

#### NF complementar de PIS/COFINS e IPI sem base de cálculo igual

- **HD:** 3022
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Comexport
- **Data abertura:** 23/02/2022
- **Problema citado:** Não é possível chegar à mesma base de PIS/COFINS; gerência pediu emitir sem base.
- **Erro apresentado:** Base de cálculo divergente na complementar.
- **Solução proposta pela Conexos:** Descobrir a base dividindo o valor do imposto pela alíquota e lançar os valores no processo (botão Despesas) como encargo diferencial, gerando a ODF a partir deles.

#### Configuração da exclusão do ICMS da base do PIS/COFINS em novos CFOPs

- **HD:** 3024
- **Tipo:** Dúvida
- **Módulo:** Fiscal
- **Cliente:** Comexport
- **Data abertura:** 24/02/2022
- **Problema citado:** Pedido de validação de todas as configurações da exclusão do ICMS da BC PIS/COFINS.
- **Solução proposta pela Conexos:** Passo a passo: na CMN_005 cadastrar encargo de identificação da redução do ICMS na base de PIS/COFINS e configurar os CFOPs conforme o guia anexado pela Conexos.

#### Diferença de centavos entre BC ICMS e total da NF (casas decimais do fator)

- **HD:** 3203
- **Tipo:** Erro/Incidente
- **Módulo:** Fiscal
- **Cliente:** Comexport
- **Data abertura:** 28/04/2022
- **Problema citado:** Diferença de R$ 0,48 entre BC do ICMS e total da NF em CFOP no modo antigo.
- **Erro apresentado:** Diferença de arredondamento.
- **Solução proposta pela Conexos:** O Conexos usa o fator com 6 casas decimais e exibe só 4, gerando a diferença. Usar o modelo de cálculo com precisão nos encargos/fator único conforme orientação.

#### CFOP fator único para não contribuinte sem DIFAL

- **HD:** 3368
- **Tipo:** Erro/Incidente
- **Módulo:** Fiscal
- **Cliente:** Comexport
- **Data abertura:** 14/06/2022
- **Problema citado:** Erro ao transmitir NF do processo 146054 sem DIFAL; incluir T-PICMSINTER no classificador 2 CAMEX resolveu. Dúvida se é correto.
- **Erro apresentado:** Erro na transmissão por falta de alíquota interestadual.
- **Solução proposta pela Conexos:** No fator único, sem DIFAL o IPI deve ficar acima da base do ICMS nos encargos do CFOP; com DIFAL a configuração muda. Seguir as variações descritas pela Conexos.

#### Validação de inconsistência entre encargo e crédito tributário no CFOP

- **HD:** 3505
- **Tipo:** Melhoria
- **Módulo:** Faturamento + NF-e
- **Cliente:** Comexport
- **Data abertura:** 14/07/2022
- **Problema citado:** Sugestão de validação quando o CFOP tributa um imposto mas o encargo não está como crédito tributário.
- **Solução proposta pela Conexos:** Escopo: parâmetro na GER_008/GER_010 com opções Nenhum/Aviso/Erro; se o encargo da GER_047 tiver valor > 0, exige Crédito tributário, Apresentação livro fiscal e Resultado fiscal = Sim.

#### Bloco K sem código do participante para itens de terceiros

- **HD:** 4021
- **Tipo:** Erro/Incidente
- **Módulo:** Fiscal
- **Cliente:** Comexport
- **Data abertura:** 03/01/2023
- **Problema citado:** SPED da filial 2 não traz o código do participante para itens com indicador 1 e 2.
- **Erro apresentado:** Código do participante vazio.
- **Solução proposta pela Conexos:** O participante é o proprietário do armazém onde está o saldo, definido no cadastro do armazém (CMN001) conforme o tipo de estoque. Revisar o cadastro do armazém.

#### Erro no registro E300 (DIFAL EC 87/15)

- **HD:** 4026
- **Tipo:** Erro/Incidente
- **Módulo:** Fiscal
- **Cliente:** Comexport
- **Data abertura:** 04/01/2023
- **Problema citado:** SPED da filial 21 com erro no E300.
- **Erro apresentado:** Registro E300 obrigatório não gerado.
- **Solução proposta pela Conexos:** O bloco só é gerado se a filial tiver inscrição estadual substituta preenchida na GER008 (botão correspondente), além das demais validações. Cadastrar a IE substituta.

#### Tags de local de entrega/retirada e NF referenciada no XML

- **HD:** 4866
- **Tipo:** Melhoria
- **Módulo:** Faturamento + NF-e
- **Cliente:** Comexport
- **Data abertura:** 14/09/2023
- **Problema citado:** Definição dos campos que alimentam as tags entrega e retirada (IMP021) e NF referenciada.
- **Solução proposta pela Conexos:** Sem solução registrada no e-mail (chamado em análise pela Conexos).

#### Registro 0220 do SPED Fiscal

- **HD:** 4988
- **Tipo:** Melhoria
- **Módulo:** SPED - EFD Fiscal
- **Cliente:** Comexport
- **Data abertura:** 18/10/2023
- **Problema citado:** Pedido de geração do 0220 (fatores de conversão) conforme Guia Prático.
- **Solução proposta pela Conexos:** Sem solução registrada no e-mail (chamado em análise pela Conexos).

#### Relatório de importação de XML da REINF em lote

- **HD:** 5068
- **Tipo:** Dúvida
- **Módulo:** Fiscal
- **Cliente:** Comexport
- **Data abertura:** 14/11/2023
- **Problema citado:** Como o relatório apresenta o campo de relação da fonte pagadora com o exterior.
- **Solução proposta pela Conexos:** Os textos foram abreviados: 'Nenhum' = Nenhum; 'A fonte pagadora é matriz da beneficiária no exterior' = Matriz benef. ext.; e assim por diante para as demais opções da CMN_025.

#### Erro na transmissão da REINF: tag paisResidExt

- **HD:** 5625
- **Tipo:** Erro/Incidente
- **Módulo:** Fiscal
- **Cliente:** Comexport
- **Data abertura:** 10/05/2024
- **Problema citado:** REINF 04/2024 da filial 13 rejeitada.
- **Erro apresentado:** País informado na tag paisResidExt diferente do esperado.
- **Solução proposta pela Conexos:** A rotina usa o campo Siscomex da CMN_020 (Países). Corrigir o código do país no cadastro (endereço do documento 192023).

#### CST de PIS/COFINS: NCM x CFOP (prioridade)

- **HD:** 5645
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Comexport
- **Data abertura:** 17/05/2024
- **Problema citado:** Sistema não acata o CST informado na tela para PIS/COFINS.
- **Erro apresentado:** CST gerado diferente do configurado.
- **Solução proposta pela Conexos:** Conforme Wiki da CTB_050, o cadastro do CFOP define se o CST é buscado primeiro da NCM ou do CFOP, pois há operações sem tributação (ex.: remessa para armazenagem).

#### Erro de custo médio ao finalizar nota (Qtd. unidades em branco)

- **HD:** 6538
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Comexport
- **Data abertura:** 14/01/2025
- **Problema citado:** Nota não finaliza por erro de custo médio.
- **Erro apresentado:** Custo médio calculado incorretamente.
- **Solução proposta pela Conexos:** Mesmo caso do HD 6026: campo 'Qtd. unidades' em branco em registro anterior à correção de ODF de embalagem. Conexos ajustou o registro; vale para documentos emitidos após o ajuste.

#### Erro no envio da REINF (evento 4020, endereço do beneficiário)

- **HD:** 7217
- **Tipo:** Erro/Incidente
- **Módulo:** Fiscal
- **Cliente:** Comexport
- **Data abertura:** 04/07/2025
- **Problema citado:** Dúvida sobre impossibilidade de enviar mais de um evento.
- **Erro apresentado:** Rejeição no registro 106 (evento 4020).
- **Solução proposta pela Conexos:** Não há limite de eventos; o erro foi endereço divergente do beneficiário (Atlantis Guarujá Terminais), já ajustado.

#### Reforma Tributária: emissão de notas de débito e crédito

- **HD:** 7901
- **Tipo:** Dúvida
- **Módulo:** Faturamento + NF-e
- **Cliente:** Comexport
- **Data abertura:** 06/01/2026
- **Problema citado:** Faltou orientação sobre campos, vínculo do documento de origem e plano contábil para ND/NC.
- **Solução proposta pela Conexos:** COM296/COM297: campo Tipo = Nota de crédito ou Nota de débito; Mais ações > Fiscal > Quadro NF-e > tipo de nota de crédito/débito. ND de pagamento antecipado: vincular em Mais ações > Docs relacionados > aba Pagamento antecipado.

#### Reforma Tributária: NF de locação com IBS/CBS

- **HD:** 7923
- **Tipo:** Dúvida
- **Módulo:** Faturamento + NF-e
- **Cliente:** Comexport
- **Data abertura:** 09/01/2026
- **Problema citado:** Dúvida se é necessário CFOP novo para notas de locação.
- **Solução proposta pela Conexos:** O sistema já tributa IBS/CBS em locação. Criar um CFOP específico para a operação, emitir nota de teste e, havendo erro, abrir novo HD.

#### Reforma Tributária: evento de aceite de débito na apuração por emissão de NC

- **HD:** 8726
- **Tipo:** Erro/Incidente
- **Módulo:** Fiscal
- **Cliente:** Comexport
- **Data abertura:** 08/07/2026
- **Problema citado:** Ajustes no evento 'Aceite de débito na apuração por emissão de nota de crédito'.
- **Erro apresentado:** Documento classificado como Comum.
- **Solução proposta pela Conexos:** Tipo do documento ajustado para Nota de débito e liberada a aba Inf. (NF-e terceiros) na COM297 > Mais ações > Fiscal quando saída, tipo ND e Própria = Não.

#### Erro ao transmitir NFS-e (filial 36, SP) - destinatário igual ao emitente

- **HD:** 8731
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Comexport
- **Data abertura:** 10/07/2026
- **Problema citado:** NFS-e 2074 transmitida com o grupo destinatário identificando a própria emitente.
- **Erro apresentado:** Inconsistência no grupo destinatário.
- **Solução proposta pela Conexos:** Testes com inclusão da tag cLocPrestacao, INDDEST = 1 e grupo Destinatário com endereço da Comexport (exigência da prefeitura). Documento 2486 seguia em análise.

#### cClassTrib 410036 (desconto incondicional) - tabela v1.60

- **HD:** 8798
- **Tipo:** Dúvida
- **Módulo:** Fiscal
- **Cliente:** Comexport
- **Data abertura:** 31/07/2026
- **Problema citado:** Se o Conexos identifica automaticamente o cClassTrib para descontos incondicionais.
- **Solução proposta pela Conexos:** O cClassTrib 410036 está cadastrado conforme Informe Técnico 2025.002 v1.60, mas o sistema não identifica automaticamente o desconto nem atribui o código ao documento; a parametrização é do usuário.

#### Reforma Tributária: escrituração de NF de terceiros (COM_243) com DFeReferenciado

- **HD:** 8827
- **Tipo:** Melhoria
- **Módulo:** Fiscal
- **Cliente:** Comexport
- **Data abertura:** 06/08/2026
- **Problema citado:** Como fica a escrituração manual de notas de terceiros na COM_243, que hoje usa a tag refNFe.
- **Solução proposta pela Conexos:** Conexos enviou escopo no Confluence (link no chamado).

#### ICMS de ativo imobilizado (MG) com alíquotas incorretas

- **HD:** 8842
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Comexport
- **Data abertura:** 10/08/2026
- **Problema citado:** ODF de ativo imobilizado em MG com ICMS incorreto (continuação do HD 7983).
- **Erro apresentado:** Valor de ICMS divergente.
- **Solução proposta pela Conexos:** Na CMN023: ICMS ação merc. = Somar; PIS/COFINS fator 2 = Não; incluído Fator IPI 1,17 com fator 1 = Sim; preparação de base aplicando fator 1; preparação de base II com IPI e THC. Diferença residual de cerca de R$ 2.

#### Exceção ao bloqueio de retenções para Simples Nacional (INSS)

- **HD:** 8906
- **Tipo:** Melhoria
- **Módulo:** Fiscal
- **Cliente:** Comexport
- **Data abertura:** 31/08/2026
- **Problema citado:** Pedido de exceção ao bloqueio de retenções do Simples na GER008 para o INSS (ex.: anexo IV).
- **Solução proposta pela Conexos:** Roteiro: se houver muitos prestadores do anexo IV, desativar a trava global 'Bloqueia retenção na provisão' e configurar as retenções por fornecedor/serviço conforme orientação da Conexos.

#### NFS-e nacional com % de ISS divergente

- **HD:** 8927
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Comexport
- **Data abertura:** 04/09/2026
- **Problema citado:** NFS-e da filial 03 subiu com ISS 3% na prefeitura e 5% no Conexos.
- **Erro apresentado:** Divergência de alíquota na apuração.
- **Solução proposta pela Conexos:** No padrão nacional o sistema não envia a alíquota; ela é definida pelo ambiente nacional conforme município e código de serviço (enviar a alíquota gera rejeição). Ajustar o cadastro interno para a alíquota correta do município.

#### Encargo ISS zerado no pedido de venda

- **HD:** 8934
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Comexport
- **Data abertura:** 08/09/2026
- **Problema citado:** Pedido de venda 17 (filial 30) não preenche o ISS, apesar do valor de referência.
- **Erro apresentado:** ISS zerado na COM034.
- **Solução proposta pela Conexos:** O ISS é calculado ao faturar o pedido: aparece zerado na COM034 e com valor na COM297 após o faturamento.

#### Reforma Tributária: NF-e de devolução com refNFe e DFeReferenciado (COM243)

- **HD:** 8938
- **Tipo:** Melhoria
- **Módulo:** Fiscal
- **Cliente:** Comexport
- **Data abertura:** 09/09/2026
- **Problema citado:** A COM243 precisa atender às tags refNFe e DFeReferenciado; ajuste só para devolução (finNFe = 4).
- **Solução proposta pela Conexos:** Escopo atualizado com validações para finNFe = 4 (devolução); demais notas mantêm refNFe. GER027, leiaute 34 e armazém da filial 30 fora do escopo. Custo absorvido pela Conexos por se tratar de reforma tributária.

#### Rejeição 657 na NFS-e SP: local de prestação no exterior (cClassTrib 410004)

- **HD:** 8964
- **Tipo:** Erro/Incidente
- **Módulo:** Faturamento + NF-e
- **Cliente:** Comexport
- **Data abertura:** 15/09/2026
- **Problema citado:** Discussão sobre a finalidade do campo de local de prestação no exterior (art. 80 da LC 214/2025).
- **Erro apresentado:** Rejeição 657: a indicação de local de prestação no exterior deve ser informada quando a classificação tributária é de exportação.
- **Solução proposta pela Conexos:** Rejeição da prefeitura, não do sistema. Com cClassTrib 410004 (CST 410, exportação) o padrão SP exige informar o local de prestação no exterior.
