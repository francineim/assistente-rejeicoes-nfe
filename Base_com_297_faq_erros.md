# COM 297 faq erros

## COM 297 faq erros

#### Qual a diferença entre os botões "Homologar" e "Finalizar"?

- **id:** COM297-FAQ-001
- **categoria:** FAQ
- **numero:** 1
- **tela_origem:** COM_297

**Solução:** O botão Homologar é utilizado para validar o documento internamente e enviá-lo para a fila de transmissão da SEFAZ (telas COM_319 ou COM_303). Já o botão Finalizar conclui o documento no sistema, gerando as movimentações financeiras e de estoque, devendo ser usado para notas que não exigem transmissão eletrônica ou após a confirmação externa da transmissão.

#### Por que os impostos (ICMS, IPI, PIS/COFINS) não foram calculados corretamente?

- **id:** COM297-FAQ-002
- **categoria:** FAQ
- **numero:** 2
- **tela_origem:** COM_297

**Solução:** O cálculo tributário na COM_297 é definido principalmente pelo CFOP selecionado. O sistema verifica a origem da alíquota seguindo uma hierarquia: primeiro verifica a DI (Importação), depois a TEC (Tarifa Externa) e, por último, a configuração do próprio CFOP (CMN_023). Verifique se o CFOP está configurado corretamente com as alíquotas desejadas.

#### Por que não consigo visualizar os títulos no financeiro após salvar a nota?

- **id:** COM297-FAQ-003
- **categoria:** FAQ
- **numero:** 3
- **tela_origem:** COM_297

**Solução:** A geração de títulos no Contas a Receber ocorre apenas após a finalização do documento. Além disso, é necessário que o campo Condição de Pagamento esteja preenchido corretamente no cabeçalho. Verifique também se o Tipo de Documento não está configurado como "Transitório", pois estes não geram lançamentos na provisão.

#### O sistema está bloqueando a homologação da nota por falta de estoque. O que fazer?

- **id:** COM297-FAQ-004
- **categoria:** FAQ
- **numero:** 4
- **tela_origem:** COM_297

**Solução:** Isso ocorre quando a trava de estoque está ativa nos "Parâmetros por Filial" (GER_008) e o produto não possui saldo suficiente. Você deve verificar a entrada da mercadoria ou ajustar o saldo antes de prosseguir, pois a COM_297 realiza a movimentação de saída (baixa) baseada no CFOP.

#### Como o sistema preenche automaticamente o CFOP na nota?

- **id:** COM297-FAQ-005
- **categoria:** FAQ
- **numero:** 5
- **tela_origem:** COM_297

**Solução:** O sistema busca o CFOP automaticamente baseando-se na tela de Configuração de Documentos (COM_065) ou através das regras de automação de pedidos (CMN_150). Caso a nota tenha origem em uma Ordem de Faturamento (ODF), o CFOP da ordem será respeitado.

#### Para notas de exportação, como preencho a "Quantidade Tributável"?

- **id:** COM297-FAQ-006
- **categoria:** FAQ
- **numero:** 6
- **tela_origem:** COM_297

**Solução:** Para notas de exportação, o campo Qtd. Trib. é obrigatório. Geralmente, ele é preenchido automaticamente com base nas configurações do cadastro do produto (COM_006), que define a unidade de medida estatística correta para o item.

#### O que impede a finalização de uma nota de retorno/devolução?

- **id:** COM297-FAQ-007
- **categoria:** FAQ
- **numero:** 7
- **tela_origem:** COM_297

**Solução:** Notas de retorno possuem validações específicas. O sistema pode bloquear a emissão se o campo "Observação da NF-e" não estiver preenchido corretamente ou se faltarem vínculos com o documento de origem.

#### Por que o benefício fiscal não foi aplicado a um item específico?

- **id:** COM297-FAQ-008
- **categoria:** FAQ
- **numero:** 8
- **tela_origem:** COM_297

**Solução:** O sistema valida o campo "Benefício" (Sim/Não) em cada item. Se houver um conflito onde a capa da nota possui um incentivo fiscal, mas o cadastro do produto está configurado sem incentivo (ou vice-versa), o sistema pode inibir a aplicação do benefício naquele item específico para garantir a integridade fiscal.

#### Erro: "NFE Municipal com quantidade de itens acima do esperado. Permitido 1. Informado: 6". O que fazer?

- **id:** COM297-ERR-001
- **categoria:** Status e Erros
- **numero:** 1
- **mensagem_erro:** NFE Municipal com quantidade de itens acima do esperado. Permitido 1. Informado: 6
- **tela_origem:** COM_297

**Solução:** Esse erro ocorre porque muitas prefeituras não aceitam notas de serviço com mais de um item. Solução: 1. Acesse a tela Cadastro de Séries Fiscais. 2. No parâmetro "Agrupar Itens Xml", selecione Sim. 3. O sistema agrupará os itens no XML (somando valores e mantendo quantidade 1) se tiverem o mesmo CFOP, %ISS, CST e Código de Serviço.

#### Erro: "Não foi possível encontrar o valor do Cofins. Configuração tributária do documento".

- **id:** COM297-ERR-002
- **categoria:** Status e Erros
- **numero:** 2
- **mensagem_erro:** Não foi possível encontrar o valor do Cofins. Configuração tributária do documento
- **tela_origem:** COM_297

**Solução:** O sistema tentou calcular o COFINS, mas encontrou percentuais ou bases zeradas nas configurações. Solução: 1. Verifique se as NCMs estão vinculadas corretamente no Classificador de Produto. 2. Valide a configuração do CFOP para garantir que o cálculo do COFINS esteja parametrizado corretamente. 3. Ambos devem ser analisados e ajustados pelo Setor Contábil/Fiscal.

#### Erro: "O tipo de serviço 'XX.XX' informado no produto 'YY' não possui código de serviço cadastrado".

- **id:** COM297-ERR-003
- **categoria:** Status e Erros
- **numero:** 3
- **mensagem_erro:** O tipo de serviço 'XX.XX' informado no produto 'YY' não possui código de serviço cadastrado
- **tela_origem:** COM_297

**Solução:** Falta o cadastro do código de serviço para a prefeitura (especialmente SP). Solução: Acesse a tela Cadastro de Classificadores de Serviço e cadastre o código de serviço correspondente, mesmo que ele já esteja informado no item da nota.

#### Erro: "A CST do ISSQN informada no produto não pode ser 'NENHUM'".

- **id:** COM297-ERR-004
- **categoria:** Status e Erros
- **numero:** 4
- **mensagem_erro:** A CST do ISSQN informada no produto não pode ser 'NENHUM'
- **tela_origem:** COM_297

**Solução:** O sistema gerou CST = -01 porque não encontrou valores válidos para o ISSQN. Solução: 1. Valide se o encargo vinculado na Parâmetros Tributários por Filial é o mesmo do CFOP/Documento. 2. No CFOP, verifique se o CST para ISSQN está correto. 3. No CFOP, verifique se o encargo no botão Encargos corresponde ao da GER_047. Se necessário, ajuste e gere a nota novamente.

#### Erro: "Finalização de N.F. com Número Fora de Sequência". Como resolver?

- **id:** COM297-ERR-005
- **categoria:** Status e Erros
- **numero:** 5
- **mensagem_erro:** Finalização de N.F. com Número Fora de Sequência
- **tela_origem:** COM_297

**Solução:** O número da nota gerada não segue a sequência esperada pelo sistema. Solução: 1. Acesse Parâmetros de Filiais > Aba ODF > Quadro Finalização de Notas Fiscais. 2. Altere "Exigir Finaliz Seq para Série" para NÃO. 3. Realize a consulta da nota na tela Geração Automática de NFe (mercadoria) ou Emissão de NF de Serviço. 4. Após processar, retorne o parâmetro para SIM.

#### Erro: "Saldo Insuficiente para o item 'X' / produto 'YYY'".

- **id:** COM297-ERR-006
- **categoria:** Status e Erros
- **numero:** 6
- **mensagem_erro:** Saldo Insuficiente para o item 'X' / produto 'YYY'
- **tela_origem:** COM_297

**Solução:** Falta saldo no armazém informado para o item. Solução: 1. Execute o procedimento "Reprocessar Ficha de Estoque Custo Médio". 2. Verifique o saldo real na tela Pesquisa de Produtos e se há reservas. 3. Se necessário, valide o parâmetro "Trava NF sem Estoque" na tela Parâmetros da Filial.

#### Erro: "O produto 'YYY' está sem lote vinculado".

- **id:** COM297-ERR-007
- **categoria:** Status e Erros
- **numero:** 7
- **mensagem_erro:** O produto 'YYY' está sem lote vinculado
- **tela_origem:** COM_297

**Solução:** O produto controla lote, mas nenhum foi informado na nota. Solução: Na tela Fiscais de Saída, selecione o item, clique no botão Lotes/Séries, depois em Vincular e selecione o lote desejado.

#### Erro: "O campo Inscrição Municipal não pode ser nulo".

- **id:** COM297-ERR-008
- **categoria:** Status e Erros
- **numero:** 8
- **mensagem_erro:** O campo Inscrição Municipal não pode ser nulo
- **tela_origem:** COM_297

**Solução:** O cadastro da filial está sem Inscrição Municipal. Solução: Acesse Cadastro de Filiais e preencha o campo "Inscrição Municipal". Se não houver, informe "ISENTO".

#### Erro: "O Cadastro do endereço 'X' da pessoa código 'x' está cancelado".

- **id:** COM297-ERR-009
- **categoria:** Status e Erros
- **numero:** 9
- **mensagem_erro:** O Cadastro do endereço 'X' da pessoa código 'x' está cancelado
- **tela_origem:** COM_297

**Solução:** O endereço vinculado à pessoa está inativo/cancelado. Solução: 1. No documento na Fiscais de Saída, ajuste o endereço pelo botão CONTABILIDADE. 2. Se gerado por ODF, verifique e ajuste na tela Cadastro de Processo > Aba Faturamento > Quadro Endereços.

#### Erro: "O campo código do Município do endereço do Destinatário não pode ser nulo".

- **id:** COM297-ERR-010
- **categoria:** Status e Erros
- **numero:** 10
- **mensagem_erro:** O campo código do Município do endereço do Destinatário não pode ser nulo
- **tela_origem:** COM_297

**Solução:** Falta o código IBGE para a cidade do destinatário. Solução: Acesse a tela Cadastro de Estados e Cidades e cadastre o código IBGE para a cidade em questão.

#### Erro: "O produto código: XXXX (Seq. xx) não está relacionado a outro(s) item(ns)".

- **id:** COM297-ERR-011
- **categoria:** Status e Erros
- **numero:** 11
- **mensagem_erro:** O produto código: XXXX (Seq. xx) não está relacionado a outro(s) item(ns)
- **tela_origem:** COM_297

**Solução:** A nota é de RETORNO e possui armazém no item, mas falta o vínculo. Solução: Vincule a nota de origem através do botão Logística > Aba Doc. Relacionados > Botão Detalhes.

#### Erro: "Nota com benefício fiscal sem itens com benefício".

- **id:** COM297-ERR-012
- **categoria:** Status e Erros
- **numero:** 12
- **mensagem_erro:** Nota com benefício fiscal sem itens com benefício
- **tela_origem:** COM_297

**Solução:** Há divergência entre o incentivo fiscal da capa da nota e do cadastro do produto. Solução: Ajuste a configuração para que sejam compatíveis: 1. Se a nota tem benefício, o produto na Cadastro de Produto > Aba VI-Fiscal deve ter incentivo (diferente de Vazio) e o CFOP deve ter incentivo (diferente de Nenhum).

#### Erro: "Item (1) está com CFOP de Exportação e sem informação de Detalhamento De Exportação".

- **id:** COM297-ERR-013
- **categoria:** Status e Erros
- **numero:** 13
- **mensagem_erro:** Item (1) está com CFOP de Exportação e sem informação de Detalhamento De Exportação
- **tela_origem:** COM_297

**Solução:** CFOPs iniciados em 7 exigem detalhamento. Solução: Na linha do item, clique no botão Exportação e preencha dados como Drawback, R.E, Chave da NF-e de entrada e Quantidade.

#### Erro: "Item (1) está com CFOP de Exportação e a quantidade tributável cadastro de produto não foi informada".

- **id:** COM297-ERR-014
- **categoria:** Status e Erros
- **numero:** 14
- **mensagem_erro:** Item (1) está com CFOP de Exportação e a quantidade tributável cadastro de produto não foi informada
- **tela_origem:** COM_297

**Solução:** Falta a unidade de medida estatística e a conversão para quantidade tributável. Solução: 1. Verifique a unidade correta da NCM na tabela da SEFAZ (ex: Kg). 2. Na Cadastro de Produto, corrija a "Unidade de Med. Estatística" e preencha a quantidade correspondente ("Qtd Trib"). 3. Na nota, os campos 'Qtd Trib', 'Unidade Trib' e 'Valor Unitário Trib' serão atualizados.

#### Erro: "O campo tributação do ICMS(CST) gerado(-01) não é válido".

- **id:** COM297-ERR-015
- **categoria:** Status e Erros
- **numero:** 15
- **mensagem_erro:** O campo tributação do ICMS(CST) gerado(-01) não é válido
- **tela_origem:** COM_297

**Solução:** O encargo ICMS está configurado para não creditar ('Crédito Tributário' = NÃO). Solução: 1. No encargo 'ICMS' do CFOP/Nota, configure a coluna 'Crédito Tributário' para SIM. 2. Verifique se o campo "Apresentação Livro Fiscal" na aba Avançados do CFOP está como SIM. 3. Regere a nota fiscal.

#### Erro: "O título código XXXX está em situação com bloqueio de Estorno/Cancelamento".

- **id:** COM297-ERR-016
- **categoria:** Status e Erros
- **numero:** 16
- **mensagem_erro:** O título código XXXX está em situação com bloqueio de Estorno/Cancelamento
- **tela_origem:** COM_297

**Solução:** A situação da duplicata impede o cancelamento (Bloqueia DOC = SIM). Solução: 1. Verifique a situação da duplicata no botão Financeiro > Quadro Quitação. 2. Acesse a tela Situação de Duplicatas e altere o campo "Bloqueia DOC" para NÃO na situação correspondente. 3. Cancele o documento financeiro na Manutenção de Títulos.

#### Erro: "Não foi possível encontrar o valor do COFINS" (CST 49).

- **id:** COM297-ERR-017
- **categoria:** Status e Erros
- **numero:** 17
- **mensagem_erro:** Não foi possível encontrar o valor do COFINS
- **tela_origem:** COM_297

**Solução:** O valor do COFINS é zero e o CST (ex: 49) exige valor. Solução: 1. Se não deve ter valor, ajuste o CST no CFOP para um que permita valor zerado (ex: 04, 06, 07, etc.). 2. Se deve ter valor, verifique as bases e alíquotas no CFOP. 3. Após ajustar o CFOP, apague e insira novamente os itens na nota.

#### Erro: "O campo alíquota do imposto do ICMS ST não pode ser nulo".

- **id:** COM297-ERR-018
- **categoria:** Status e Erros
- **numero:** 18
- **mensagem_erro:** O campo alíquota do imposto do ICMS ST não pode ser nulo
- **tela_origem:** COM_297

**Solução:** O CFOP usa CST 90 ("Outros"), que exige o envio das tags de ICMS e ICMS ST, mesmo que zeradas. Solução: 1. Se possível, use outro CST recomendado pelo contador. 2. Se deve usar CST 90, inclua os encargos de ICMS, Base ICMS, Base ICMS ST e ICMS ST no cadastro do CFOP (CMN_023), marcando 'Crédito Tributário = SIM'. 3. Refature a nota ou reinsira os itens.

#### Erro: "O CFOP utilizado está configurado para utilizar um Incentivo Fiscal diferente do utilizado no documento".

- **id:** COM297-ERR-019
- **categoria:** Status e Erros
- **numero:** 19
- **mensagem_erro:** O CFOP utilizado está configurado para utilizar um Incentivo Fiscal diferente do utilizado no documento
- **tela_origem:** COM_297

**Solução:** Divergência entre o incentivo na capa da nota e no CFOP. Solução: Verifique qual está correto e ajuste: 1. Se o documento estiver correto: Ajuste o campo "Incentivo Fiscal" no CFOP. 2. Se o CFOP estiver correto: Ajuste o campo "Incentivo Fiscal" no botão Contabilidade da nota. 3. Finalize o documento.

#### Erro: "Não foi possível encontrar o valor do PIS" (CST 49).

- **id:** COM297-ERR-020
- **categoria:** Status e Erros
- **numero:** 20
- **mensagem_erro:** Não foi possível encontrar o valor do PIS
- **tela_origem:** COM_297

**Solução:** O valor do PIS é zero e o CST (ex: 49) exige valor. Solução: Mesma solução do COFINS: Ajuste o CST para um que aceite valor zerado ou corrija o cálculo para gerar valor. Reinserir os itens após ajuste.

#### Erro: "Este documento está configurado para não enviar o campo 'Informações adicionais do produto'".

- **id:** COM297-ERR-021
- **categoria:** Status e Erros
- **numero:** 21
- **mensagem_erro:** Este documento está configurado para não enviar o campo 'Informações adicionais do produto'
- **tela_origem:** COM_297

**Solução:** A opção de gerar info adicional está desmarcada. Solução: 1. No botão 'Propriedades' do documento, marque o checkbox "Gerar Info Adic.". 2. Se gerado por ODF, verifique se a opção está marcada na Aba Faturamento do Cadastro do Processo.

#### Erro: "O produto código: X esta com valor (1,00) abaixo do custo (2,00)".

- **id:** COM297-ERR-022
- **categoria:** Status e Erros
- **numero:** 22
- **mensagem_erro:** O produto código: X esta com valor (1,00) abaixo do custo (2,00)
- **tela_origem:** COM_297

**Solução:** O sistema bloqueia vendas com valor unitário menor que o custo médio. Solução: 1. Verifique se o custo está correto. Se necessário, execute o "Reprocessa Ficha de Estoque - Custo Médio". 2. Para liberar, altere para NÃO o parâmetro "De Saída com Valores Unitários Abaixo do Custo" na tela Parâmetros de Filiais > Faturamento > Quadro Bloqueia Finalização.

#### Erro: "O campo Data de Registro da DI/DSI/DA não pode ser nulo".

- **id:** COM297-ERR-023
- **categoria:** Status e Erros
- **numero:** 23
- **mensagem_erro:** O campo Data de Registro da DI/DSI/DA não pode ser nulo
- **tela_origem:** COM_297

**Solução:** Falta a data de registro na DI vinculada. Solução: Acesse a tela Cadastro da D.I e utilize o procedimento "Incluir Data de Registro na DI" para preencher a informação.

#### Erro: "O valor para o campo 'Descrição do Produto' não pode ser nulo".

- **id:** COM297-ERR-024
- **categoria:** Status e Erros
- **numero:** 24
- **mensagem_erro:** O valor para o campo 'Descrição do Produto' não pode ser nulo
- **tela_origem:** COM_297

**Solução:** A filial exige a descrição da DI, mas a nota é manual e não tem DI vinculada. Solução: 1. Copie a descrição do produto. 2. Cole no campo "Complemento" do item na nota. 3. Salve e homologue.

#### Erro: "O campo valor do ICMS não pode ser nulo".

- **id:** COM297-ERR-025
- **categoria:** Status e Erros
- **numero:** 25
- **mensagem_erro:** O campo valor do ICMS não pode ser nulo
- **tela_origem:** COM_297

**Solução:** Erro na configuração para anulação de frete (Produto/CFOP como Serviço). Solução: 1. O produto deve ter Tipo = "Produto Revenda". 2. O CFOP deve ter "Livro Fiscal" = "Mercadoria" e "Apresentação Livro Fiscal" = "Sim" para o ICMS. 3. Homologue o documento.

#### Erro: "Não Existe Saldo (por Processo) para o produto: XXXX".

- **id:** COM297-ERR-026
- **categoria:** Status e Erros
- **numero:** 26
- **mensagem_erro:** Não Existe Saldo (por Processo) para o produto: XXXX
- **tela_origem:** COM_297

**Solução:** A filial controla estoque por processo e não há saldo para o processo informado. Solução: 1. Valide o saldo na Pesquisa de Produtos > Aba Estoque por Processo. 2. Para liberar (com saldo negativo), altere para NÃO o parâmetro "Controla Estoque" no quadro Estoque por Processo da Parâmetros da Filial. Atenção: Retorne para SIM após finalizar.

#### Erro: "O campo tributação do IPI(CST) não pode ser nulo".

- **id:** COM297-ERR-027
- **categoria:** Status e Erros
- **numero:** 27
- **mensagem_erro:** O campo tributação do IPI(CST) não pode ser nulo
- **tela_origem:** COM_297

**Solução:** O parâmetro "EXIGE CST DA IPI NA NFE" está ativo na GER_008, mas o IPI não foi calculado na nota. Solução: 1. Se a nota não deve ter IPI, altere o parâmetro na Parâmetros por Filial para NÃO. 2. Se deve ter IPI, ajuste o CFOP para calcular o encargo.

#### Erro: "O campo Alíquota Pis / Cofins (em percentual) não pode ser nulo".

- **id:** COM297-ERR-028
- **categoria:** Status e Erros
- **numero:** 28
- **mensagem_erro:** O campo Alíquota Pis / Cofins (em percentual) não pode ser nulo
- **tela_origem:** COM_297

**Solução:** CST 49 exige envio de alíquota e base. Solução: Verifique se o CFOP tem base, percentual e valor configurados para PIS/COFINS. Ajuste o CFOP e refaça o item/nota.

#### Erro: "O cadastro da série fiscal é diferente do exigido para NF-e".

- **id:** COM297-ERR-029
- **categoria:** Status e Erros
- **numero:** 29
- **mensagem_erro:** O cadastro da série fiscal é diferente do exigido para NF-e
- **tela_origem:** COM_297

**Solução:** A sigla da série fiscal está incorreta. Solução: Acesse Cadastro de Série Fiscal e corrija o campo "Sigla para Impressão no Livro Fiscal" para um valor numérico entre 000-889.

#### Erro: "Quando houver industrialização, o armazém de origem... deve ser informado".

- **id:** COM297-ERR-030
- **categoria:** Status e Erros
- **numero:** 30
- **mensagem_erro:** Quando houver industrialização, o armazém de origem... deve ser informado
- **tela_origem:** COM_297

**Solução:** O sistema entende como industrialização se o produto da nota for diferente do produto vinculado no retorno. Solução: Se for apenas devolução, o produto na nota e no vínculo (Docs Relacionados) deve ser o mesmo. Se forem diferentes, informe o armazém de origem no item.

#### Erro: "Os valores totais de DÉBITO e CRÉDITO estão divergentes para o Lote".

- **id:** COM297-ERR-031
- **categoria:** Status e Erros
- **numero:** 31
- **mensagem_erro:** Os valores totais de DÉBITO e CRÉDITO estão divergentes para o Lote
- **tela_origem:** COM_297

**Solução:** Configuração contábil do CFOP está desbalanceada. Solução: 1. Corrija os lançamentos no botão Contabilidade do CFOP. 2. Na nota, vá em Mais Ações > Contabilidade > "Recontabilizar Doc". 3. Finalize.

#### Erro: "Documentos com títulos com números repetidos".

- **id:** COM297-ERR-032
- **categoria:** Status e Erros
- **numero:** 32
- **mensagem_erro:** Documentos com títulos com números repetidos
- **tela_origem:** COM_297

**Solução:** A condição de pagamento está gerando títulos com o mesmo número da nota, causando duplicidade. Solução: 1. Na Condição de Pagamento, altere o campo "GERAÇÃO TÍTULO" para "NUMERO DOCUMENTO + ORDEM" (ou outra variação). 2. Na nota, vá no botão Financeiro e clique em Regerar. 3. Finalize.

#### Erro: "A habilitação para NFE informada na filial expirou".

- **id:** COM297-ERR-033
- **categoria:** Status e Erros
- **numero:** 33
- **mensagem_erro:** A habilitação para NFE informada na filial expirou
- **tela_origem:** COM_297

**Solução:** O cadastro na tela Regime NF-e venceu. Solução: Cadastre um novo regime na Regime NF-e (não cancele o anterior). Atenção: Não pode haver notas em "HOMOLOGAÇÃO" ou "HOM. CANCELAMENTO" durante este processo.

#### Erro: "O tipo de documento informado no C.F.O.P. não está compatível com tipo de documento da nota fiscal!".

- **id:** COM297-ERR-034
- **categoria:** Status e Erros
- **numero:** 34
- **mensagem_erro:** O tipo de documento informado no C.F.O.P. não está compatível com tipo de documento da nota fiscal!
- **tela_origem:** COM_297

**Solução:** Incompatibilidade entre o tipo de documento da nota e o configurado no CFOP. Solução: Ajuste o CFOP para usar o tipo de documento correto ou altere o tipo de documento da nota para corresponder ao CFOP.

#### Erro: "Documentos Relacionados - COM_302: O documento possui vínculos de retorno detalhado!".

- **id:** COM297-ERR-035
- **categoria:** Status e Erros
- **numero:** 35
- **mensagem_erro:** Documentos Relacionados - COM_302: O documento possui vínculos de retorno detalhado!
- **tela_origem:** COM_297

**Solução:** Tentativa de vincular documento na capa (retorno total) e nos itens (retorno parcial) simultaneamente. Solução: Use apenas um local: 1. Devolução total: Use o quadro "Documento Retorno" na COM_091. 2. Devolução parcial: Use a aba "Vínculo dos Itens da NF" na COM_122.

#### Erro: "Produto(s) com 'Origem da Mercadoria' marcado como 'NENHUM'".

- **id:** COM297-ERR-036
- **categoria:** Status e Erros
- **numero:** 36
- **mensagem_erro:** Produto(s) com 'Origem da Mercadoria' marcado como 'NENHUM'
- **tela_origem:** COM_297

**Solução:** O produto está sem origem definida. Solução: Ajuste o campo "Origem Mercadoria" na tela Cadastro de Produtos > Aba VI-Fiscal. Se a nota for importada via XML, o sistema pode não buscar a origem automaticamente; nesses casos, ajuste manualmente ou recrie a nota.

#### Erro: "O campo do endereço do destinatário não pode ser nulo".

- **id:** COM297-ERR-037
- **categoria:** Status e Erros
- **numero:** 37
- **mensagem_erro:** O campo do endereço do destinatário não pode ser nulo
- **tela_origem:** COM_297

**Solução:** O cadastro da pessoa está sem número no endereço. Solução: 1. Na Cadastro de Pessoas, cancele o endereço incorreto e cadastre novamente com o número preenchido. 2. Na nota, vá em Mais Ações > Contabilidade, busque o endereço atualizado e salve.

#### Erro: "O campo valor por unidade tributável não pode ser nulo".

- **id:** COM297-ERR-038
- **categoria:** Status e Erros
- **numero:** 38
- **mensagem_erro:** O campo valor por unidade tributável não pode ser nulo
- **tela_origem:** COM_297

**Solução:** CST 99 (Outras Saídas) para IPI exige valor. Solução: Verifique com o setor fiscal. Se não houver IPI, altere o CST para "Não Tributada" ou similar no CFOP.

#### Erro: "Não é Permitido Utilizar este tipo de Documento em um Documento Fiscal".

- **id:** COM297-ERR-039
- **categoria:** Status e Erros
- **numero:** 39
- **mensagem_erro:** Não é Permitido Utilizar este tipo de Documento em um Documento Fiscal
- **tela_origem:** COM_297

**Solução:** O Tipo de Documento está configurado como "Quitação de Adiantamento = SIM". Solução: Altere o campo "Quit. Saldo de Adto" para NÃO na tela Tipos de Documentos. Refature a ODF e transmita a NF.

#### Erro: "Alterar Processo do Documento - PRS_073" (Bloqueio).

- **id:** COM297-ERR-040
- **categoria:** Status e Erros
- **numero:** 40
- **mensagem_erro:** Alterar Processo do Documento - PRS_073
- **tela_origem:** COM_297

**Solução:** Não é possível alterar o processo se ele for de exportação ou se houver vínculo com ODF. Solução: Verifique na aba Itens se há vínculo com "Ordem de FAT". Se houver, o vínculo com a ODF impede a alteração do processo.

#### Erro: "Existem lançamentos vinculados a processos com data de fechamento contábil informada".

- **id:** COM297-ERR-041
- **categoria:** Status e Erros
- **numero:** 41
- **mensagem_erro:** Existem lançamentos vinculados a processos com data de fechamento contábil informada
- **tela_origem:** COM_297

**Solução:** O borderô possui baixas vinculadas a processos fechados contabilmente. Solução: 1. Cancele/Estorne o borderô e finalize segregado (uma baixa por documento). 2. Ou realize a abertura do fechamento contábil do processo.

#### Erro: "Produto com Lote/Série inativo".

- **id:** COM297-ERR-042
- **categoria:** Status e Erros
- **numero:** 42
- **mensagem_erro:** Produto com Lote/Série inativo
- **tela_origem:** COM_297

**Solução:** O lote vinculado está inativo. Solução: Ative novamente o lote/série na tela correspondente.

#### Erro: "O produto XXXXXX não tem saldo suficiente no lote".

- **id:** COM297-ERR-043
- **categoria:** Status e Erros
- **numero:** 43
- **mensagem_erro:** O produto XXXXXX não tem saldo suficiente no lote
- **tela_origem:** COM_297

**Solução:** Saldo insuficiente no lote específico. Solução: Verifique a movimentação no relatório RP_CTB_032. Se não houver saldo, use um CFOP que não movimente estoque (Estoque Contábil = NÃO) ou ajuste o saldo.

#### Erro: "O documento não pode ser finalizado, pois o produto... encontra-se sem o armazém de destino".

- **id:** COM297-ERR-044
- **categoria:** Status e Erros
- **numero:** 44
- **mensagem_erro:** O documento não pode ser finalizado, pois o produto... encontra-se sem o armazém de destino
- **tela_origem:** COM_297

**Solução:** O CFOP "Gerencia Estoque em Poder de Terceiros" = SIM, exigindo armazém de destino. Solução: Informe o armazém de destino nos itens ou, se incorreto, altere o parâmetro no CFOP para NÃO.

#### Erro: "O centro de custos não foi informado para o Item 1".

- **id:** COM297-ERR-045
- **categoria:** Status e Erros
- **numero:** 45
- **mensagem_erro:** O centro de custos não foi informado para o Item 1
- **tela_origem:** COM_297

**Solução:** O Tipo de Documento exige Centro de Custo (Configuração "Ambos" ou "Fiscal"). Solução: Informe o centro de custo no item ou altere a configuração "Exige Centro de Custo" na tela Tipos de Documentos para NÃO.

#### Erro: "Item (X) sem incidência de beneficio fiscal".

- **id:** COM297-ERR-046
- **categoria:** Status e Erros
- **numero:** 46
- **mensagem_erro:** Item (X) sem incidência de beneficio fiscal
- **tela_origem:** COM_297

**Solução:** Divergência entre "Benefício Fiscal" no documento (NÃO) e "Incentivo Fiscal" no produto (Preenchido). Solução: Ajuste para ficarem iguais: 1. Marque "Benefício Fiscal" = SIM no item do documento. 2. Ou limpe o campo "Incentivo Fiscal" no cadastro do produto.

#### Erro: "Descontos/Incentivos Fiscais - COM_015 - NÃO FOI ENCONTRADO CONFIGURAÇÃO PARA O DOCUMENTO".

- **id:** COM297-ERR-047
- **categoria:** Status e Erros
- **numero:** 47
- **mensagem_erro:** Descontos/Incentivos Fiscais - COM_015 - NÃO FOI ENCONTRADO CONFIGURAÇÃO PARA O DOCUMENTO
- **tela_origem:** COM_297

**Solução:** Falta configuração de descontos no cadastro da pessoa. Solução: Acesse Cadastro de Pessoas > Mais Ações > Comissões > Documentos Financeiros e configure os dados necessários.

#### Erro: "A data de movimento da NF-e difere da data de movimento no botão fiscal...".

- **id:** COM297-ERR-048
- **categoria:** Status e Erros
- **numero:** 48
- **mensagem_erro:** A data de movimento da NF-e difere da data de movimento no botão fiscal...
- **tela_origem:** COM_297

**Solução:** A data de emissão excede a tolerância em relação à homologação (notas retroativas). Solução: Acesse Parâmetros de Filiais e defina o campo "Gera Data Movimento na Nota Fiscal Eletrônica" como "Sim, com avisos".

#### Erro: "A quantidade de itens da nota deve possuir no máximo 4 casas decimais".

- **id:** COM297-ERR-049
- **categoria:** Status e Erros
- **numero:** 49
- **mensagem_erro:** A quantidade de itens da nota deve possuir no máximo 4 casas decimais
- **tela_origem:** COM_297

**Solução:** Este erro ocorre na homologação porque o sistema (seguindo regra da SEFAZ) valida a quantidade de casas decimais na coluna de quantidade. A SEFAZ não aceita NF-e com mais de 4 casas decimais na quantidade comercial. Solução: Ajuste a quantidade do item na nota fiscal para ter, no máximo, 4 casas decimais.

#### Erro: "Serviço Indisponível". O que fazer?

- **id:** COM297-ERR-050
- **categoria:** Status e Erros
- **numero:** 50
- **mensagem_erro:** Serviço Indisponível
- **tela_origem:** COM_297

**Solução:** Esta mensagem geralmente ocorre quando o certificado digital na base do cliente encontra-se vencido, ou caso seja um cliente novo e o certificado nunca foi vinculado. Solução: Acesse a tela Certificado para Faturamento e insira um novo certificado com vencimento válido.

#### Erro Validando Arquivo Xml - Xbairro: "Viola A Restrição Minlength De '2'".

- **id:** COM297-ERR-051
- **categoria:** Status e Erros
- **numero:** 51
- **mensagem_erro:** Viola A Restrição Minlength De '2'
- **tela_origem:** COM_297

**Solução:** O bairro do destinatário tem menos de 2 caracteres. Solução: 1. Acesse a tela Cadastro de Pessoas > Botão Endereço. 2. Cancele o endereço incorreto e cadastre um novo corrigindo a descrição do bairro. 3. Na nota fiscal, vá em "Mais Ações" > "Contabilidade", atualize o endereço e salve antes de transmitir.

#### Erro Gerando XML - Gerando EMIT/C16: Fone.

- **id:** COM297-ERR-052
- **categoria:** Status e Erros
- **numero:** 52
- **mensagem_erro:** Gerando XML - Gerando EMIT/C16: Fone.
- **tela_origem:** COM_297

**Solução:** Falta o telefone no cadastro da filial (se NF própria) ou da pessoa (se NF de Terceiros). Solução: 1. NF Própria: Insira o número de telefone na tela Cadastro de Filiais. 2. NF de Terceiros: Insira o telefone na aba dados básicos e no botão Endereço da tela Cadastro de Pessoas.

#### Erro Gerando XML - Gerando EMIT/C01.

- **id:** COM297-ERR-053
- **categoria:** Status e Erros
- **numero:** 53
- **mensagem_erro:** Gerando XML - Gerando EMIT/C01.
- **tela_origem:** COM_297

**Solução:** O cadastro da filial está incompleto. Solução: Acesse a tela Cadastro de Filiais e preencha todos os campos obrigatórios.

#### Erro Gerando XML - Gerando DET_PROD/I01 (Msg #171).

- **id:** COM297-ERR-054
- **categoria:** Status e Erros
- **numero:** 54
- **mensagem_erro:** Gerando XML - Gerando DET_PROD/I01 (Msg #171).
- **tela_origem:** COM_297

**Solução:** Existem produtos na nota fiscal sem a informação de NCM. Solução: Acesse a tela Cadastro de Produtos e preencha o campo NCM para todos os produtos envolvidos no faturamento.

#### Erro Gerando XML - Gerando DET_PROD/I01 (Msg #161).

- **id:** COM297-ERR-055
- **categoria:** Status e Erros
- **numero:** 55
- **mensagem_erro:** Gerando XML - Gerando DET_PROD/I01 (Msg #161).
- **tela_origem:** COM_297

**Solução:** Erro na geração da descrição complementar do produto para o XML. Solução: Verifique as configurações de descrição de produtos na NF-e e ajuste conforme as orientações do sistema.

#### Erro Gerando XML - Gerando IPITRIB/O07.

- **id:** COM297-ERR-056
- **categoria:** Status e Erros
- **numero:** 56
- **mensagem_erro:** Gerando XML - Gerando IPITRIB/O07.
- **tela_origem:** COM_297

**Solução:** Configurações do encargo de IPI estão incorretas no CFOP. Solução: No CFOP, verifique:
- Se há valor e percentual para Base IPI e Valor IPI.
- Se 'Crédito Tributário' está marcado como Sim.
- Se o campo 'Livro Fiscal' na aba Avançados está Sim.
- Se o CST e enquadramento de IPI estão corretos.

#### Erro Gerando XML - Gerando PISOUTR/Q05.

- **id:** COM297-ERR-057
- **categoria:** Status e Erros
- **numero:** 57
- **mensagem_erro:** Gerando XML - Gerando PISOUTR/Q05.
- **tela_origem:** COM_297

**Solução:** CSTs 71, 72 e 74 exigem o envio de valores de PIS/COFINS, mesmo que zerados. Solução: Inclua os encargos de BC, % e Valor de PIS/COFINS no CFOP e reinsira os itens na nota para atualizar as configurações.

#### Erro Gerando XML - Gerando DET_PROD_DI/I18.

- **id:** COM297-ERR-058
- **categoria:** Status e Erros
- **numero:** 58
- **mensagem_erro:** Gerando XML - Gerando DET_PROD_DI/I18.
- **tela_origem:** COM_297

**Solução:** A URF de despacho informada no BL ou na DI não possui UF vinculada. Solução: Acesse a tela Cadastro de URF e inclua a informação da UF na URF utilizada, ou preencha a URF Despacho no BL.

#### Erro Gerando XML - Gerando ICMSUFDEST/NA01.

- **id:** COM297-ERR-059
- **categoria:** Status e Erros
- **numero:** 59
- **mensagem_erro:** Gerando XML - Gerando ICMSUFDEST/NA01.
- **tela_origem:** COM_297

**Solução:** O CFOP está configurado como Consumidor Final (= Sim), exigindo cálculo de DIFAL, mas os encargos não foram encontrados. Solução: 1. Verifique se a operação é realmente para consumidor final. 2. Configure os encargos de DIFAL no CFOP conforme a tela Parâmetros Tributários > Aba Trib. III. 3. Verifique a Inscrição Estadual do destinatário.

#### Erro: "{http://www.portalfiscal.inf.br/nfe:nre}' is expected".

- **id:** COM297-ERR-060
- **categoria:** Status e Erros
- **numero:** 60
- **mensagem_erro:** {http://www.portalfiscal.inf.br/nfe:nre}' is expected
- **tela_origem:** COM_297

**Solução:** Falta o Número do RE (Registro de Exportação) em uma nota de exportação. Solução: Na tela Fiscais de Saída, na linha do item, clique no botão Exportação e informe o Número do RE.

#### Erro Validando Arquivo Xml - Ufterceiro.

- **id:** COM297-ERR-061
- **categoria:** Status e Erros
- **numero:** 61
- **mensagem_erro:** Validando Arquivo Xml - Ufterceiro.
- **tela_origem:** COM_297

**Solução:** O campo "Encomendante Adquirente" no Processo está com uma pessoa do exterior (UF = EX), o que não é permitido para este campo na NF-e. Solução: Acesse a tela Cadastro de Processo, ajuste o campo Encomendante Adquirente para uma pessoa nacional, salve e homologue a nota novamente.

#### Erro Validando Arquivo Xml - nSeqAdic.

- **id:** COM297-ERR-062
- **categoria:** Status e Erros
- **numero:** 62
- **mensagem_erro:** Validando Arquivo Xml - nSeqAdic.
- **tela_origem:** COM_297

**Solução:** O número sequencial do item dentro da Adição (DI) está incorreto (ex: veio o código do produto "15599" em vez de sequencial "1"). Solução: 1. Na tela Ordem de Faturamento, cancele a nota. 2. Na aba Mercadorias, exclua e inclua os itens novamente para corrigir a sequência. 3. Fature a ODF novamente.

#### Erro: "O elemento '{htp://...}cExportador não é esperado".

- **id:** COM297-ERR-063
- **categoria:** Status e Erros
- **numero:** 63
- **mensagem_erro:** O elemento '{htp://...}cExportador não é esperado
- **tela_origem:** COM_297

**Solução:** Conflito de informações no XML (informação de DI onde não deveria ou vice-versa). Solução: Se a nota não deve ter dados de DI, retire as informações de D.I. da linha dos itens. Se deve ter, certifique-se de que o processo está vinculado no cabeçalho.

#### Erro: "Falha da análise do elemento {htp://...}fone".

- **id:** COM297-ERR-064
- **categoria:** Status e Erros
- **numero:** 64
- **mensagem_erro:** Falha da análise do elemento {htp://...}fone
- **tela_origem:** COM_297

**Solução:** O telefone do destinatário contém caracteres inválidos ou espaços. Solução: Acesse o botão Endereços na tela Cadastro de Pessoas, corrija o telefone e atualize o endereço na nota (ou edite a ODF).

#### Erro: "Falha Da Análise Do Elemento '{Http://...}Serie' Com Valor 'Nf'".

- **id:** COM297-ERR-065
- **categoria:** Status e Erros
- **numero:** 65
- **mensagem_erro:** Falha Da Análise Do Elemento '{Http://...}Serie' Com Valor 'Nf'
- **tela_origem:** COM_297

**Solução:** O Modelo Fiscal da série selecionada na nota é diferente do modelo da nota original vinculada (devolução). Solução: Ajuste a Série Fiscal e o Tipo de Documento para terem o mesmo modelo fiscal da nota original (ex: 55).

#### Erro gerando XML: "is not a valid integer value".

- **id:** COM297-ERR-066
- **categoria:** Status e Erros
- **numero:** 66
- **mensagem_erro:** is not a valid integer value
- **tela_origem:** COM_297

**Solução:** Geralmente ocorre por letras em campos numéricos ou falta da "Via de Transporte". Solução: Informe a Via de Transporte na tela Logística (vinculada ao processo) e tente transmitir novamente.

#### Erro: "Falha da análise do elemento '{htp://...}xPed' com valor...".

- **id:** COM297-ERR-067
- **categoria:** Status e Erros
- **numero:** 67
- **mensagem_erro:** Falha da análise do elemento '{htp://...}xPed' com valor...
- **tela_origem:** COM_297

**Solução:** O número do Pedido do Cliente contém caracteres inválidos ou excede 15 dígitos. Solução: 1. Cancele a NF e a programação. 2. Corrija o campo 'Pedido Cliente NR' na tela Pedido de Venda. 3. Refaça o faturamento.

#### Erro: "Falha da análise do elemento '{htp://...}'Orig' com valor '6'".

- **id:** COM297-ERR-068
- **categoria:** Status e Erros
- **numero:** 68
- **mensagem_erro:** Falha da análise do elemento '{htp://...}'Orig' com valor '6'
- **tela_origem:** COM_297

**Solução:** A origem da mercadoria enviada é '6', mas a SEFAZ espera 0, 1 ou 2 para esta operação. Solução: Verifique e ajuste a "Origem da Mercadoria" na tela Cadastro de Produto > Aba VI-Fiscal.

#### Erro: "Falha da análise do elemento '{htp://...}CST' com valor '73'".

- **id:** COM297-ERR-069
- **categoria:** Status e Erros
- **numero:** 69
- **mensagem_erro:** Falha da análise do elemento '{htp://...}CST' com valor '73'
- **tela_origem:** COM_297

**Solução:** O CST de PIS/COFINS enviado (73) é inválido para a operação (esperado 99). Solução: Acesse o CFOP > Aba SPED/NFE e ajuste os campos de PIS e COFINS para o CST correto (ex: 99).

#### Erro: "Falha Da Análise Do Elemento '{http://...}xcpl' Com Valor...".

- **id:** COM297-ERR-070
- **categoria:** Status e Erros
- **numero:** 70
- **mensagem_erro:** Falha Da Análise Do Elemento '{http://...}xcpl' Com Valor...
- **tela_origem:** COM_297

**Solução:** O complemento do endereço excede o limite de 60 caracteres. Solução: 1. Acesse Cadastro de Pessoas, duplique o endereço e ajuste o complemento para ter menos de 60 caracteres. 2. Na nota, use o botão Contabilidade para selecionar o novo endereço e salve.

#### Erro: "yErrText=Gerando ICMSUFDest/NA01".

- **id:** COM297-ERR-071
- **categoria:** Status e Erros
- **numero:** 71
- **mensagem_erro:** yErrText=Gerando ICMSUFDest/NA01
- **tela_origem:** COM_297

**Solução:** Falta configuração de encargos para DIFAL (ICMSUFDest) no CFOP. Solução: Configure os encargos de partilha de ICMS (DIFAL) no Cadastro de CFOP conforme a Nota Técnica 2015/003.

#### Erro Validando Arquivo Xml - Modelo (Restrição 55).

- **id:** COM297-ERR-072
- **categoria:** Status e Erros
- **numero:** 72
- **mensagem_erro:** Validando Arquivo Xml - Modelo (Restrição 55).
- **tela_origem:** COM_297

**Solução:** A nota de devolução não possui série cadastrada ou o modelo não é 55, ou falta a chave de acesso. Solução: 1. Cadastre a série com modelo 55 na tela Séries Fiscais. 2. Insira a chave de acesso da nota original no botão Propriedades da Fiscais de Saída.

#### Erro: "Código CEST não informado".

- **id:** COM297-ERR-073
- **categoria:** Status e Erros
- **numero:** 73
- **mensagem_erro:** Código CEST não informado
- **tela_origem:** COM_297

**Solução:** Produto sujeito a substituição tributária sem CEST informado. Solução: Preencha o campo "ICMS/CEST" na tela Cadastro de Produto > Aba VI-Fiscal. Se o produto tiver CEST mas não precisar destacar, informe "00000000".

#### Erro: "Número de série inválido".

- **id:** COM297-ERR-074
- **categoria:** Status e Erros
- **numero:** 74
- **mensagem_erro:** Número de série inválido
- **tela_origem:** COM_297

**Solução:** O campo "Modelo" na série fiscal está preenchido incorretamente (ex: "002"). Solução: Ajuste o campo Modelo na tela Cadastro de Séries para o valor correto (ex: "2").

#### Erro: "Motivo: O encargo está com valor negativo".

- **id:** COM297-ERR-075
- **categoria:** Status e Erros
- **numero:** 75
- **mensagem_erro:** Motivo: O encargo está com valor negativo
- **tela_origem:** COM_297

**Solução:** Algum cálculo de encargo resultou em valor negativo no XML. Solução: Verifique as configurações de impostos e descontos no botão Encargos e ajuste para que o valor final seja positivo.

#### Erro: "Motivo: A data de fabricação do lote está incorreta".

- **id:** COM297-ERR-076
- **categoria:** Status e Erros
- **numero:** 76
- **mensagem_erro:** Motivo: A data de fabricação do lote está incorreta
- **tela_origem:** COM_297

**Solução:** A data de fabricação do lote é inválida (ex: ano 0219). Solução: Corrija a data no botão Lotes/Séries da tela Cadastro de Produto e vincule novamente na nota.

#### Erro: "Motivo: Ausência de CNPJ ou número incorreto".

- **id:** COM297-ERR-077
- **categoria:** Status e Erros
- **numero:** 77
- **mensagem_erro:** Motivo: Ausência de CNPJ ou número incorreto
- **tela_origem:** COM_297

**Solução:** O CNPJ da pessoa na nota está incorreto ou em branco. Solução: Valide e corrija o número do documento federal na tela Cadastro de Pessoas.

#### Erro: "O CFO selecionado está configurado para utilizar outro armazém".

- **id:** COM297-ERR-078
- **categoria:** Status e Erros
- **numero:** 78
- **mensagem_erro:** O CFO selecionado está configurado para utilizar outro armazém
- **tela_origem:** COM_297

**Solução:** O CFOP exige um "Armazém Origem" específico que diverge do informado ou está em branco. Solução: Ajuste o CFOP na tela CFOP para "Tipo de Armazém Origem" = Sugestivo, ou informe o armazém correto na nota fiscal.

#### Erro: "CVC-PATTERN-VALID... IDESTRANGEIRO".

- **id:** COM297-ERR-079
- **categoria:** Status e Erros
- **numero:** 79
- **mensagem_erro:** CVC-PATTERN-VALID... IDESTRANGEIRO
- **tela_origem:** COM_297

**Solução:** O campo "Nº doc. exterior (TIN)" no endereço da pessoa contém informação inválida. Solução: Cadastre um novo endereço deixando o campo TIN em branco (se não for obrigatório) ou corrija o valor. Atualize o endereço na nota/ODF.

#### Erro: "NÃO FOI POSSÍVEL INICIAR O ROBÔ: FALHA NA COMUNICAÇÃO RPC".

- **id:** COM297-ERR-080
- **categoria:** Status e Erros
- **numero:** 80
- **mensagem_erro:** NÃO FOI POSSÍVEL INICIAR O ROBÔ: FALHA NA COMUNICAÇÃO RPC
- **tela_origem:** COM_297

**Solução:** Incompatibilidade ou versão desatualizada do Java no ambiente do Robô. Solução: Instale a versão atualizada do Java (Java 21), reinicie o computador e teste o robô novamente.

#### Erro: "Erro na execução do robô - Error Executing Transaction".

- **id:** COM297-ERR-081
- **categoria:** Status e Erros
- **numero:** 81
- **mensagem_erro:** Erro na execução do robô - Error Executing Transaction
- **tela_origem:** COM_297

**Solução:** O certificado digital vinculado à tela de Eventos venceu. Solução: Valide e atualize o certificado na tela Eventos e Certificados.

#### Erro: "Erro transmitindo nota: O servidor enviou o código de status 403: Forbidden".

- **id:** COM297-ERR-082
- **categoria:** Status e Erros
- **numero:** 82
- **mensagem_erro:** Erro transmitindo nota: O servidor enviou o código de status 403: Forbidden
- **tela_origem:** COM_297

**Solução:** O certificado digital utilizado é inválido ou o CNPJ do certificado não corresponde ao emitente do XML. Solução: Atualize o certificado digital na tela Gerência de Certificados, garantindo que corresponda ao CNPJ da filial emitente.

#### Erro: "ERRO GERANDO XML: NO ENUM CONSTANT... TUF.1".

- **id:** COM297-ERR-083
- **categoria:** Status e Erros
- **numero:** 83
- **mensagem_erro:** ERRO GERANDO XML: NO ENUM CONSTANT... TUF.1
- **tela_origem:** COM_297

**Solução:** A UF da placa do veículo na transportadora está preenchida incorretamente com o valor "1". Solução: Na tela Fiscais de Saída, clique no botão Logística, selecione a Transportadora e corrija o campo "UF" da Placa Veículo para a sigla correta (ex: SP).

#### Erro: "Existem erros que impedem o cancelamento do documento" (Vínculo NF Serviço x Mercadoria).

- **id:** COM297-ERR-084
- **categoria:** Status e Erros
- **numero:** 84
- **mensagem_erro:** Existem erros que impedem o cancelamento do documento
- **tela_origem:** COM_297

**Solução:** Este erro ocorre quando a nota fiscal de serviço possui vínculo com uma nota fiscal de mercadoria, impedindo o cancelamento padrão. Solução: Atualmente, para desfazer esse vínculo específico e permitir o cancelamento, a correção deve ser realizada via programação/suporte técnico.

#### Erro: "Existem erros que impedem o cancelamento... o documento possui títulos parametrizados para cobrança".

- **id:** COM297-ERR-085
- **categoria:** Status e Erros
- **numero:** 85
- **mensagem_erro:** Existem erros que impedem o cancelamento... o documento possui títulos parametrizados para cobrança
- **tela_origem:** COM_297

**Solução:** O cancelamento foi confirmado na SEFAZ/Prefeitura, mas o pedido continua preso no status de cancelamento no sistema porque os títulos financeiros estão vinculados a uma remessa bancária/cobrança. Solução: 1. Acesse a tela Gerência de Títulos, pesquise o documento e marque o checkbox. 2. Vá em "Mais Ações" > "Gerenciar" e altere os campos "Cancelar Vínculo com Lote" e "Cancelar Cobrança de títulos" para Sim. 3. Acesse o botão "Alteração de Carteira" > quadro "Remover da Carteira" e altere para Sim. 4. Após o ajuste, retorne à tela Geração Automática de NF-e > Mais Ações > Situação NF-e > Consultar. O status deve atualizar para "Cancelado".

#### Erro: "CVC-COMPLEX-TYPE.2.4.A: INVALID CONTENT WAS FOUND STARTING WITH ELEMENT' {"HTTP://WWW.PORTALFISCAL.INF.BR/NFE":GIBSUF}'. ONE OF '{"HTTP://WWW.P

- **id:** COM297-ERR-086
- **categoria:** Status e Erros
- **numero:** 86
- **mensagem_erro:** CVC-COMPLEX-TYPE.2.4.A: INVALID CONTENT WAS FOUND STARTING WITH ELEMENT' {"HTTP://WWW.PORTALFISCAL.INF.BR/NFE":GIBSUF}'. ONE OF '{"HTTP://WWW.PORTALFISCAL.INF.BR/NFE":VBC}' IS EXPECTED
- **tela_origem:** COM_297
- **observacao:** ATENÇÃO: a resposta publicada na wiki não corresponde ao erro (trata de baixa/variação cambial na FIN010, não da rejeição de schema gIBSUF/vBC). Revisar antes de usar.

**Solução:** Quando o sistema processa a baixa, ele aplica a seguinte lógica para solucionar o cálculo e definição de contas: primeiramente, obtém o plano financeiro associado ao contrato de câmbio, que será utilizado no campo Conta Financeira de Baixa da FIN010; em seguida, identifica que a DI possui data de CI, indicando que existe uma conta em andamento; depois, verifica que o título possui taxa registrada e confirma que a data de CI (14/11/2025) é anterior à data de fechamento do contrato de câmbio (26/11/2025), além de validar que ambas pertencem ao mesmo mês e ano (11/2025); então, a partir do documento vinculado (11), o sistema obtém a conta correspondente ao primeiro lançamento para registrar o desconto; por fim, realiza o cálculo da variação, aplicando a fórmula: Variação = (Valor da baixa / taxa do título) * (taxa da DI / taxa do título).

#### Erro: "A DATA DE VENCIMENTO ESTÁ MENOR QUE A DE LANÇAMENTO DO DOCUMENTO!" (ERRO ou AVISO)

- **id:** COM297-ERR-087
- **categoria:** Status e Erros
- **numero:** 87
- **mensagem_erro:** A DATA DE VENCIMENTO ESTÁ MENOR QUE A DE LANÇAMENTO DO DOCUMENTO!
- **tela_origem:** COM_297
- **observacao:** Item sem numeração na wiki; numerado como 87 na extração. Mensagem pode aparecer como ERRO ou AVISO.

**Solução:** Essas mensagens podem ser exibidas quando o parâmetro Crítica Data Vencimento x Data Lançamento, disponível na tela de Parâmetros da Filial > quadro "Configuração de Títulos", estiver configurado como Aviso ou Erro.
A validação compara a data de vencimento do título com a data de lançamento do documento. Quando a data de vencimento é inferior à data de lançamento, o sistema identifica uma inconsistência e apresenta a mensagem correspondente à configuração definida no parâmetro.
- Se configurado como Aviso, o sistema apenas alerta o usuário sobre a inconsistência encontrada.
- Se configurado como Erro, o sistema bloqueia a finalização ou homologação do documento até que a situação seja corrigida.
Para esta comparação, o sistema considera os seguintes campos de lançamento:
- Tela de Documentos Fiscais de Entrada e Financeiro a Pagar → campo Data Entrada.
- Tela de Documentos Fiscais de Saída e Financeiro a Receber → campo Data Saída.
