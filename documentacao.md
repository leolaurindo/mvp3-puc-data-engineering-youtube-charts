# O exercício

O professor solicitou que

# Documentação
---

1. Encontrando os dados

O primeiro passo foi extrair os dados da página `charts.youtube.com`. Optei por utilizar o `selenium web-driver`.

Cada página permite baixar um .csv, e cada página semanal é formada por uma url padrão + as datas de referência. Para facilitar nossa vida, essas datas se encontram na aba `"networks"` do `DevTools`. Copiei e colei no arquivo `reference_dates.json`.

![Aba networks](screenshots/1.png)

Num projeto contínuo, esse seria o primeiro passo e, para evitar esse passo manual, o ideal é que o scrap seja rodado semanalmente. Assim, a extração dos dados combinará com a página inicial que a url `charts.youtube.com` abrirá.

Para fins desse exercício, também extrairei o `payload` manualmente. Os dados, entretanto, podem ser adquiridos com requests pela api do youtube. Como já farei alguns requests, não quero extrapolar o número limite (10.000 diários), por isso farei por esse método.

