# Validações cadastradas

## Validações cadastradas pela equipe

#### NFE DE AJUSTE SEM DOCUMENTO VINCULADO

**Causa:** Estamos gerando uma nota fiscal de ajuste utilizando o PRS_025, e estamos devolvendo apenas alguns itens da nota fiscal mãe. Quando eu vou homologar o documento o sistema não permite pois o valor da nota fiscal de ajuste é diferente da nota fiscal original. Então eu fiz o vinculo por item (COM_122), mas ao tentar homologar o documento o sistema retorna com um novo erro: "NFE DE AJUSTE SEM DOCUMENTO VINCULADO".

Como eu fiz o vínculo por item, não posso fazer o vínculo na COM_302.

**Solução:** A Nota Fiscal de Ajuste é um documento eletronico (modelo 55) usado exclusivamente para regularizaçoes de ordem contabil, fiscal ou de apuraçao de tributos, sem que haja circulaçao fisica de mercadorias.

Estorno de venda: Quando a nota original nao pode ser cancelada no prazo legal e a mercadoria ainda nao saiu da empresa.

Ou seja, o estorno é total da nota fiscal original, dessa forma, o vinculo deve ser feito em Documentos Relacionados > quadro "DOCUMENTO RETORNO".

Para um movimento parcial, deve ser feita uma nota fiscal de devoluçao.

#### remessa para industrialização

**Solução:** Utilizar o CFOP 5924
