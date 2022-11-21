# Flask Steam
## Features
- Busca de jogos na Steam
- Exibindo preços nas lojas do Brasil e Argentina
- Converte para real para comparar se vale a pena comprar na outra loja
- Salvar favoritos

Entrar na pasta flask_steam
```
cd flask_steam
```

Executa migrações no banco de dados
```
flask db upgrade 
```

Inicia projeto
```
flask run
```

## Tests

```
python -m pytest --cov=flask_steam
```
