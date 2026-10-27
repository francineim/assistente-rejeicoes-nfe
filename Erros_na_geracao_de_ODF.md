# Erros na geração de ODF — Conexos

> Fonte: Wiki Conexos (wiki.conexos.cloud/index.php/Erros_na_geração_de_ODF) — extraído em 27/10/2026

## Índice

1. Não foi encontrado nenhum item com saldo para gerar a ODF
2. Falta a série fiscal (saída) no processo
3. Falta o tipo de operação no processo
4. Falta configuração geral ou em filial
5. Não há itens para gerar ODF com os parâmetros informados
6. Não foi possível ligar os itens à ordem de faturamento complementar
7. Cliente não possui incentivo fiscal cadastrado
8. Condição de pagamento inválida/inexistente no cadastro de cliente
9. Existe variável inválida (xxx) configurada no CFOP
10. Não é permitido faturar ODF com configuração de Automação de NFS-e
11. Existem produtos duplicados nessa ordem de faturamento
12. Quantidade do campo "Rateio Qtd. Vol." da INVOICE difere da quantidade faturada
13. Deve-se agrupar NF por INVOICE (rateio qtd. vol. por INVOICE)
14. Cadastro de Pessoa não encontrado
15. Centro de Custo está nulo
16. Falta Data da C.I na D.I.
17. Processo não está liberado para "(Cadastro de Pessoas)"
18. Item sem peso líquido informado
19. A DI cadastrada nos itens não está válida para o processo
20. Nenhum lote ativo foi encontrado para vincular ao produto
21. Erro na geração da NF — Condição de Pagamento inválida (Cód. ODF)
22. Erro ao faturar ODF complementar de exportação
23. Ausência de imposto para NF de mercadoria na Configuração de ODF
24. Itens sem Benefício Fiscal e CST (ICMS) = -01
25. Tag "ITEMLISTASERVICO" obrigatória (máx. 5 caracteres)
26. "GERANDO ID (CUF)"
27. Procedimento cancelado pelo Usuário!
28. Processo não liberado para faturamento!
29. Falta a Série Fiscal (Saída) no Processo! (aba DUIMP / Operação Triangular)
30. Endereço de origem inativo sem endereço ativo equivalente

---

## 1. Erro gerando ordem de faturamento: Não foi encontrado nenhum item com saldo para gerar a ODF

Ao gerar uma ODF através do botão Geração Automática, ocorre o erro acima.

![Erro 1 – Tela do erro](imagens/odf_01_a.png)

**Causa:**

Deverá verificar as ODF de entrada e saída geradas para o processo e checar se ainda há saldo entre DI x ODF. Ou seja, se ainda possui saldo de ODF. Mesmo que tenha saldo no Armazém do Processo (estoque), o sistema gera a mensagem de erro caso não tenha saldo de ODF x DI.

```
Exemplificando para melhor entendimento:
---------------
Produto XXXX com 1.000 unidades:
(+) 1.000 ( ODF de entrada )
(-) 1.000 ( ODF de saída )
(=) 0 ( Resultado > SALDO DE ODF = ZERO )
---------------
```

**Solução:**

Deverá utilizar a opção = NÃO do check box **Utilizar Saldo de Produtos** e tentar novamente gerar a ODF.

![Erro 1 – Opção "Utilizar Saldo de Produtos"](imagens/odf_01_b.png)

> **IMPORTANTE** — Se estiver utilizando Configuração de Ordem de Faturamento:
> - Deverá se atentar se a configuração de ODF estiver configurada com opção = SIM.
> - Pois se estiver, ao utilizar o campo = NÃO, quando informar a configuração de ODF, irá retornar para = SIM.
> - Desta forma, deverá: ou ajustar a configuração de ODF ou não utilizar.

---

## 2. Falta a série fiscal (saída) no processo!!!

Ao gerar uma ODF através do botão Geração Automática, ocorre o erro abaixo:

```
Erro ao executar consulta: FALTA A SERIE FISCAL (SAÍDA) NO PROCESSO !!!
```

**Causa:**

Ao verificar o Processo (Cadastro Processo) informado na geração da ODF, identifica-se que na aba Faturamento, nos campos Série NF Entrada e Série NF Saída, não consta informação da Série Fiscal para NF.

![Erro 2 – Cadastro do Processo – séries de entrada/saída](imagens/odf_02_a.png)

**Solução:**

Acessar a Tela Cadastro Processo > Aba Faturamento > Campo Série NF Saída e incluir a série utilizada para emissão de Notas Fiscais. Em seguida, gerar a ODF novamente.

---

## 3. Falta o tipo de operação no processo!!!

Ao gerar uma ODF através do botão Geração Automática, ocorre o erro acima.

![Erro 3 – Tela do erro](imagens/odf_03_a.jpeg)

**Causa:**

Ao verificar o Processo (Cadastro Processo) informado na geração da ODF, identifica-se que na aba Faturamento, nos campos Série NF Entrada e Série NF Saída, Tipo Operação e Estoque não existem informação.

![Erro 3 – Correção no Cadastro do Processo](imagens/odf_03_b.png)

**Solução:**

Acessar a Tela Cadastro Processo > Aba Faturamento > Campos Série NF Entrada e Série NF Saída, Tipo Operação e Estoque e incluir as informações para emissão de Notas Fiscais. Em seguida, gerar a ODF novamente.

---

## 4. Falta configuração geral ou em filial!!!

Ao gerar uma ODF através do botão Geração Automática, ocorre o erro acima.

![Erro 4 – Tela do erro](imagens/odf_04_a.png)

**Causa:**

Este erro ocorre porque não existe série de romaneio cadastrada na tela de Parâmetros por Filial.

**Solução:**

Deverá acessar a tela de Parâmetros Gerais > Geração Ordem de Faturamento e verificar se há informações nos campos abaixo:

- Tipo de Operação
- Tipo de Documento

Caso estejam sem informação, deverão ser preenchidos.

---

## 5. Não há itens para gerar ODF com os parâmetros informados!!!

**Causa:**

1. Confirmar se a finalidade do processo está como **Exportação**.
2. Validar o cadastro da Invoice de Exportação no Quadro: Importador > Campo: Endereço.

**Solução:**

Para o ajuste do endereço deve retirar o visto da Invoice, visto que não tem como realizar alterações com visto. Em seguida realizar os devidos ajustes. Gere o visto novamente para que o processo seja apresentado e seja possível faturá-lo.

---

## 6. Erro ao executar consulta: não foi possível ligar os itens à ordem de faturamento complementar!!!

**Causa:**

A D.I na tela de Cadastro de D.I possui uma sequência válida para o processo diferente da sequência no qual a nota fiscal que está sendo complementada foi emitida.

**Solução:**

Tornar a sequência da D.I válida na mesma sequência da nota que está sendo complementada.

---

## 7. Erro geração ODF - cliente não possui incentivo fiscal cadastrado (cadastro de pessoas/botão "desconto")!!!

**Causa:**

Ao gerar uma ODF ocorre o erro citado devido à configuração na Tela Cadastro de Parâmetros da Filial > Aba ODF > Campo **TRAVA FATURAMENTO SEM CONF. REPASSE** igual a 'SIM'.

**Solução:**

Para que o erro não persista, deverá alterar o Campo **TRAVA FATURAMENTO SEM CONF. REPASSE** para **NÃO** e em seguida gerar a ODF.

---

## 8. Erro na geração da NF!! Condição de pagamento inválida no cadastro de cliente! Condição de pagamento inexistente no cadastro de cliente!

**Causa:**

Esta mensagem aparece porque no cadastro da Pessoa selecionada na Ordem de Faturamento — Aba Financeiros > Quadro Créditos A Receber > Botão Créditos A Pagar e Receber — não existe informação de Condição de Pagamento cadastrada.

**Solução:**

Acessar a Aba Financeiros > Quadro Créditos A Receber > Botão Créditos A Pagar e Receber e cadastrar a mesma condição de pagamento que foi selecionada na Ordem de Faturamento.

---

## 9. Erro na geração da NF!! Existe variável inválida (xxx), configurada no CFOP!

**Causa:**

Esta mensagem aparece porque no cadastro da Pessoa selecionada na Ordem de Faturamento — Aba Financeiros > Quadro Créditos A Receber > Botão Créditos A Pagar e Receber — não existe informação de Condição de Pagamento cadastrada.

**Solução:**

Acessar a Aba Financeiros > Quadro Créditos A Receber > Botão Créditos A Pagar e Receber e cadastrar a mesma condição de pagamento que foi selecionada na Ordem de Faturamento.

> *Observação: na wiki, a causa e a solução deste erro estão idênticas às do item 8 (possível duplicação no conteúdo original).*

---

## 10. Cadastro de Ordem de Faturamento. Não é permitido faturar uma ordem de faturamento que possua configuração para gerar Automação de NFSE! Código X

![Erro 10 – Tela do erro](imagens/odf_10_a.png)

**Causa:**

Esta mensagem ocorre pois na Tela Configuração de Ordem de Faturamento está parametrizado para gerar automaticamente uma NF de Serviço.

**Solução:**

Deverá acessar a Tela Configuração de Ordem de Faturamento e verificar o campo descrito abaixo:

**Automação NF Serviço:** Este parâmetro é para emissão automática de NF Serviço quando o Processo for Conta e Ordem de Terceiros.

- Se este parâmetro estiver definido como SIM, ao gerar uma NF de Saída referente à mercadoria na Tela Geração de Ordem de Faturamento, automaticamente será gerada uma NF de Serviço com Status igual a Homologação. Esta ação irá ocorrer no momento ao clicar no Botão Faturar a NF (Saída) de Mercadoria.
- Quando a escolha para este parâmetro for igual a NÃO, permanece o funcionamento padrão do sistema, gerando somente a NF de Saída referente à mercadoria.

Caso o mesmo esteja configurado igual a **SIM**, haverá necessidade de cancelar a Configuração de Ordem de Faturamento, cadastrar uma nova e alterar o campo supracitado para **NÃO**.

Em seguida, prosseguir com a geração do documento via ODF.

---

## 11. Erro na geração da NF!! Existem produtos duplicados nessa ordem de faturamento.!

**Causa:**

Esta mensagem ocorre pois existe mais de um produto com o mesmo código.

**Solução:**

Deverá acessar a Tela Cadastro por Filiais > Quadro ODF > Campo Bloqueia Repetir Produtos para **Não**.

Em seguida, prosseguir com a geração do documento via ODF.

---

## 12. Cadastro de ordem de faturamento - Atenção! Quantidade definida no campo "Rateio Qtd. Vol." no cadastro da INVOICE: XXXX, difere da quantidade de itens faturados da ordem de faturamento a ser gerada!!!

![Erro 12 – Tela do erro](imagens/odf_12_a.png)

**Causa:**

O erro ocorre pois o processo está configurado de forma errada. Esse erro se refere à Tela Cadastro de Processos > Acordeon II - Faturamento > Campo Rateio Qtd. Vol.

**Solução:**

Há duas opções para solucionar esse problema:

- **A) D.I.:** opção default e faz o funcionamento atual de rateio dos volumes da D.I. para as NF-e.
- **B) INVOICE:** nesta opção, o sistema vai ratear os volumes para a NF-e utilizando a informação do campo 'Quantidade Volume' que consta na INVOICE.
  - Quando no campo 'Rateio Qtd. Vol.' da Tela Cadastro de Ordem de Faturamento > Botão Geração Automática o usuário escolher a opção agrupar NF INVOICE, o sistema irá validar se todos os itens da INVOICE estão sendo faturados.
  - Caso contrário, o sistema irá apresentar erro, não permitindo faturar.

Ao gerar a ODF o campo 'Agrupar NF por INVOICE' estará igual a sim, porém para este processo existe apenas 1 INVOICE.

Portanto a configuração do campo 'Rateio Qtd. Vol.' no processo deve ser D.I.

Alterando para D.I. como meio de validação, a ODF será gerada corretamente.

---

## 13. Cadastro de ordem de faturamento - Erro gerando ODF: Deve-se agrupar NF por INVOICE, pois no processo o rateio qtd. vol. está configurado por INVOICE.

![Erro 13 – Tela do erro](imagens/odf_13_a.png)

**Causa:**

O erro ocorre pois o processo está configurado com Rateio Qtd. Vol. igual a INVOICE na Tela Cadastro de Processos > Acordeon II - Faturamento > Campo Rateio Qtd. Vol., e no Botão Geração Automática da Tela Ordem de Faturamento foi informado "não" no campo Agrupar NF por INVOICE.

**Solução:**

Na Geração Automática da ODF, o campo agrupar por INVOICE deve estar marcado como sim, pois na Tela Cadastro de Processo está definido por INVOICE; caso contrário, o erro irá persistir.

---

## 14. Cadastro de Ordem de Faturamento. Erro: Cadastro de Pessoa não Encontrado!

![Erro 14 – Tela do erro](imagens/odf_14_a.png)

**Causa:**

Esta mensagem ocorre pois no processo vinculado à Ordem de Faturamento há um contrato vinculado e neste contrato não consta a pessoa cadastrada na Tela Cadastro de Contratos > Aba Pessoas.

**Solução:**

1. Acessar a Tela Cadastro de Processo e verificar qual o contrato vinculado.
2. Acessar a Tela Cadastro de Contratos, pesquisar o contrato desejado e, na aba pessoas, vincular a pessoa que está sendo informada na ODF.
3. Prosseguir com o cadastro / alteração da ODF.

---

## 15. Centro de Custo está nulo, por favor preencha esse campo na tela de Processo ou na tela de Cadastro de Pessoa no botão filiais! Código da ordem de faturamento x

![Erro 15 – Tela do erro](imagens/odf_15_a.png)

**Causa:**

A mensagem apresentada não se trata de erro, mas de uma nova validação disponibilizada no sistema.

**Solução:**

Esta mensagem irá ocorrer no faturamento de ODF - NF Serviço, pois o Campo Centro de Custo passou a ser obrigatório.

> Observação: A tag do XML `<UFDESEMB>` da NF de Mercadoria considera o campo "UF".

Quando ocorrer, deverão ser validados 2 campos na tela de Cadastro de Parâmetros de Filiais - Gerais:

- **Travar ODF Serviço sem Dados Obrigatórios?:** Se estiver como SIM, alterar para NÃO.
- **Pedido de Venda/ODF - Exige Centro de Custo:** Se estiver como SIM, alterar para NÃO.

---

## 16. Cadastro de Ordem de Faturamento - Falta Data da C.I na D.I.!!!

![Erro 16 – Tela do erro](imagens/odf_16_a.png)

**Causa:**

A mensagem apresentada é devido à falta de informações na Tela Cadastro de DI / DSI.

**Solução:**

Neste caso, deverá proceder da seguinte forma:

- Acessar a Tela Cadastro de DI / DSI
- Pesquisar a DI desejada
- Verificar o campo Data da CI
- Caso esteja em branco, poderá inserir manualmente a data caso ainda não tenha sido desembaraçada
- Ou proceder com a consulta da mesma na Tela Siscomex Web - Importação de DI para atualizar a Data da CI

---

## 17. Cadastro de Ordem de Faturamento - Erro: Este processo não está liberado para "(Cadastro de Pessoas)".

![Erro 17 – Tela do erro](imagens/odf_17_a.png)

**Causa:**

Esse erro ocorre devido a uma configuração no cadastro de pessoa (Tela Cadastro de Pessoa > Acordeon Importação/Exportação > Bloqueio Processo).

**Solução:**

Para que possa prosseguir com o faturamento, vá na Tela Liberação de Processo - Faturamento/Operacional > Pesquisar > Faturamento = NÃO > Liberar.

Para maiores informações sobre a Tela IMP097, acessar o link: https://wiki.conexos.info/index.php/IMP_097

---

## 18. Faturamento da ODF X para o processo XXX - item sem peso líquido informado (Adição: X / Item X).

![Erro 18 – Tela do erro](imagens/odf_18_a.png)

**Causa:**

A mensagem apresentada é devido à falta de peso líquido na Tela Cadastro de DI / DSI > Aba Itens > Campo Peso Líquido.

**Solução:**

- Acessar a Tela Cadastro de DI / DSI
- Pesquisar a DI desejada
- Acessar a Aba Itens
- Editar o item e incluir o peso líquido

---

## 19. Faturamento da ODF 1 para o Processo 3 - Erro na geração da NF: a DI cadastrada nos itens não está válida para o processo.

![Erro 19 – Tela do erro](imagens/odf_19_a.png)

**Causa:**

O erro ocorre pois a DI vinculada à ODF não está registrada como válida na Tela Cadastro de D.I./D.S.I.

**Solução:**

Deverá ir na Tela Cadastro de D.I./D.S.I. > DI Válida para o Processo e alterar para SIM.

---

## 20. Faturamento da ODF X para o processo XXX - Nenhum lote ativo foi encontrado para vincular ao produto !!!!

![Erro 20 – Tela do erro](imagens/odf_20_a.png)

**Causa:**

Este erro ocorre quando é informado armazém de origem e destino e não é vinculado lote em um item da invoice.

**Solução:**

Vincule o lote na invoice para validação.

> Obs.: A validação é disparada quando se está fazendo uma saída e a mesma possui armazém de destino, ou se está fazendo uma entrada que tenha armazém de destino. Sendo assim, quando o sistema encontra algum produto que não possui vínculo de lote com a invoice, ele gera o erro.

---

## 21. Faturamento da ODF X para o processo XX - Erro na geração da NF!!

**Mensagem apresentada:** Faturamento da ODF X para o processo XX - Erro na geração da NF !! Condição de Pagamento inválida no cadastro de cliente! Condição de Pagamento inexistente no cadastro de cliente ! Cód. ODF: 3.

![Erro 21 – Tela do erro](imagens/odf_21_a.png)

**Causa:**

Este erro ocorre quando as informações cadastradas na tela de Cadastro de Pessoas estão divergentes do que está na ODF.

**Solução:**

Para resolução você deve optar por uma das opções abaixo:

- Incluir na tela de Cadastro de Pessoas > botão "Mais Ações" > "Crédito a Receber" > aba "Condição de Pagamento CMN_170" a condição de pagamento saída Cta e Ordem s/câmbio;
- Ou limpar o campo da condição de pagamento e cancelar a informação na aba "Condição de Pagamento".

---

## 22. Erro ao faturar ODF complementar de exportação

```
Mensagem: "FATURAMENTO DA ODF 3 PARA O PROCESSO X - NAO FOI POSSIVEL GERAR A ORDEM DE
FATURAMENTO, POIS NAO FOI ENCONTRADO NA TELA IMPORTAÇÃO DE NF-E/NFS-E UM DOCUMENTO
GERADO COM A CHAVE "X"."
```

**Causa:**

O erro ocorre pois há uma divergência na origem da mercadoria, pois o sistema realiza uma validação usando o classificador e o tipo de operação; sendo assim, o campo "Origem" dessas opções não pode estar marcado como "NENHUM".

**Solução:**

Acesse a tela de Parâmetros Gerais → **Tratamento dos Itens na Importação do XML**. Este parâmetro faz várias validações nos itens e verifica os que estão em uma ODF de exportação; o erro é gerado pois não encontra a nota de entrada na tela Importação de NF-e / NFS-e. Desta forma, para dar seguimento, é necessário configurar este parâmetro para **"NÃO"** e faturar a ODF.

---

## 23. Erro na ausência de imposto para nota fiscal de mercadoria na tela de configuração de ordem de faturamento

```
Mensagem: "A Nota Fiscal de Mercadoria não possui nenhum imposto que atenda as configurações
feitas na tela de Configuração de Ordem de Faturamento! Códigos dos encargos da NFE".
```

![Erro 23 – Tela do erro](imagens/odf_23_a.png)

**Causa:**

Esse erro ocorre quando o valor das despesas é lançado com o valor incorreto. Isso acaba ocasionando a inexistência de impostos na tela de Configuração de Ordem de Faturamento, e acontece quando o usuário possui na tela de Cadastro de Pessoa > Acordeon "Importação/Exportação" > botão "Configuração ODF com valor a faturar apontado para o serviço" a informação que seria a Configuração de ODF.

Dentre as diversas validações que o sistema realiza antes da Geração do Faturamento de Serviço, uma delas é verificar se o documento gerado pela ODF de Mercadoria possui nos Encargos o mesmo encargo configurado na tela de Configuração de Ordem de Faturamento > quadro "Configuração de Automação NF Serviços", e que o seu valor em moeda negociada seja maior que zero. Além disso, o valor do encargo que gera a Tributação da Nota de Mercadoria deve estar zerado.

**Solução:**

Para a resolução, valide as informações acima.

---

## 24. Erro: Existem itens sem o Benefício Fiscal preenchido e pelo menos um dos produtos possui CST (ICMS) = -01.

**Causa:**

Este erro ocorre devido ao fato de que na tela IMP_206 (Controle da Finalização do Contrato de Câmbio), a rotina cria a ODF vinculada ao "CÓD. CONTRATO DE CÂMBIO" e "CÓD. VARIAÇÃO CAMBIAL", criando despesa no processo também vinculada ao "CÓD. CONTRATO DE CÂMBIO" e ao "CÓD. VARIAÇÃO CAMBIAL" com o mesmo valor da variação cambial apresentada na IMP_206. Desta forma, ao faturar essa ODF que foi gerada da IMP_206, são levadas as despesas que foram criadas no processo a partir do mesmo registro da IMP_206.

**Solução:**

Deve ser feito o cancelamento da despesa dentro do Processo, cancelar a finalização do contrato de câmbio e aplicar a variação novamente; desta forma essa despesa será aplicada no faturamento.

---

## 25. Erro: "ERRO AO MONTAR NOTAS - EXCEPTION: PARA ESSA CIDADE O CAMPO REFERENTE A TAG "ITEMLISTASERVICO" É OBRIGATÓRIO E NÃO DEVE SER MAIOR QUE 5 CARACTERES"

```
SCRIPT: LOADENVIOARQUIVO: "..\\COMUNS\\ROTINASLERSETARCAMPOS.TXT" LINHA: 406 COLUNA: 7
```

![Erro 25 – Tela do erro](imagens/odf_25_a.png)

**Causa:**

Este erro é referente a um código do serviço configurado fora do padrão estipulado pelo **Planalto**.

**Solução:**

É necessário acessar o Cadastro de Produto > acordeon "VI - Fiscal" > campo "Cod. Serviço por Filial", e alinhar o código com o padrão.

---

## 26. Erro: "GERANDO ID (CUF)"

![Erro 26 – Tela do erro](imagens/odf_26_a.png)

**Causa:**

Este erro ocorre pois a pessoa vinculada à operação não está com o estado (UF) cadastrado em seu endereço.

**Solução:**

Realize o ajuste no cadastro na tela de Cadastro de Pessoas > botão "Endereços".

---

## 27. Erro: Procedimento cancelado pelo Usuário!

**Causa:**

A rotina de faturamento está programada para verificar o status de bloqueio do processo conforme a configuração feita na tela de Cadastro de Pessoas, no acordeom "Importação/Exportação", campo "Bloqueio Processo", onde:

1. Verifica primeiro a pessoa encomendante do processo.
2. Se não houver, verifica a pessoa do processo.

**Comportamento do campo "Bloqueio Processo":**

- **Operacional:** Bloqueia o faturamento
- **Não:** Permite o faturamento
- **Faturamento:** Verifica se o processo está liberado para faturamento

**Solução:**

- Acesse a tela de Cadastro de Pessoas.
- Vá até o acordeom "Importação/Exportação".
- Localize o quadro "Bloqueio Processo".
- Verifique o valor do campo "Bloqueio Processo" para:
  - A pessoa encomendante do processo.
  - Se não houver, para a pessoa do processo.

**Ajuste necessário:**

- Se o campo estiver como "Operacional", altere para:
  - "Não" → se deseja liberar o faturamento sem restrições.
  - "Faturamento" → se deseja permitir faturamento apenas quando o processo estiver liberado.

---

## 28. Erro: Processo não liberado para faturamento! (Revise as configurações do Processo e Pessoa/Encomendante)

**Causa:**

A rotina de faturamento está programada para verificar o status de bloqueio do processo conforme a configuração feita na tela de Cadastro de Pessoas, no acordeom "Importação/Exportação", campo "Bloqueio Processo", onde:

1. Verifica primeiro a pessoa encomendante do processo.
2. Se não houver, verifica a pessoa do processo.

**Comportamento do campo "Bloqueio Processo":**

- **Operacional:** Bloqueia o faturamento
- **Não:** Permite o faturamento
- **Faturamento:** Verifica se o processo está liberado para faturamento

**Solução:**

- Acesse a tela de Cadastro de Pessoas.
- Vá até o acordeom "Importação/Exportação".
- Localize o quadro "Bloqueio Processo".
- Verifique o valor do campo "Bloqueio Processo" para:
  - A pessoa encomendante do processo.
  - Se não houver, para a pessoa do processo.

**Ajuste necessário:**

- Se o campo estiver como "Operacional", altere para:
  - "Não" → se deseja liberar o faturamento sem restrições.
  - "Faturamento" → se deseja permitir faturamento apenas quando o processo estiver liberado.

---

## 29. Erro: Falta a Série Fiscal (Saída) no Processo! (aba DUIMP / Operação Triangular)

**Causa:**

Ao tentar gerar a ODF na tela Cadastro de Ordem de Faturamento, aba DUIMP, o sistema realiza uma validação das configurações vinculadas à ODF.

Quando a configuração de ODF possui o parâmetro **Operação Triangular** ativo (quadro Mais Dados), o sistema exige que o campo **Configuração de ODF Secundária** esteja devidamente preenchido. Quando o campo não estiver preenchido, a geração da ODF é bloqueada. Quando o campo estiver corretamente informado, a validação é liberada e a ODF pode ser gerada normalmente.

**Solução:**

1. Acesse a tela de Cadastro de Ordem de Faturamento > aba "Duimp" > quadro "Mais Dados" e verifique se o parâmetro Operação Triangular está ativo.
2. Caso esteja ativo, localize o campo "Configuração de ODF Secundária".
3. Preencha o campo com a configuração correspondente sempre que o parâmetro "Operação Triangular" estiver ativo.
4. Após o preenchimento, a validação deixa de ocorrer.

---

## 30. Mensagem de erro: "O endereço de origem está inativo e não existe endereço ativo equivalente para sugestão automática. Favor cadastrar ou selecionar outro endereço."

**Contexto:**

A partir da versão V36600 está aplicada uma rotina de validação para que a geração de ODFs **valide o campo "Endereço"** e o substitua automaticamente caso esteja inativo.

Primeiro o sistema verifica se existe endereço ativo na tela de Cadastro de Pessoas para a **mesma pessoa, com mesmo Nº Documento Federal, cidade e estado** do endereço inativo:

- Se existir, acontece automaticamente a sugestão deste endereço no lugar do inativo.
- Se existir mais de um, não sugere nada.
- **Se não existir, é exibida esta mensagem de erro.**

---

## Referências Internas

- Cadastro de Processos
- Configuração de Ordem de Faturamento
- Ordem de Faturamento
- Invoice de Exportação
- Cadastro de D.I
- Créditos A Pagar E Receber
- Cadastro de Pessoas
- Variáveis de CFOP
- Cadastro de CFOP
