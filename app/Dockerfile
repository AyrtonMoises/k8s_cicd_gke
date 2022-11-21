FROM python:3.10

# Cria usuario, pasta e define como proprietario
RUN useradd -ms /bin/bash user-app \
    && mkdir /flask_steam \
    && chown user-app: /flask_steam

# Instala gunicorn para ser servidor
RUN pip install gunicorn

# Copia os arquivos do projeto para o diretorio do app
COPY --chown=user-app /flask_steam/ /flask_steam

# Definindo diretorio
WORKDIR /flask_steam

# Copia arquivo de requirements
COPY requirements.txt requirements.txt

# Instalando os requerimentos com o PIP
RUN pip install --no-cache-dir --upgrade -r requirements.txt


# Seta locale
RUN apt-get clean && apt-get update && apt-get install -y locales
RUN sed -i '/pt_BR.UTF-8/s/^# //g' /etc/locale.gen && \
    locale-gen
ENV LANG pt_BR.UTF-8
ENV LANGUAGE pt_BR:pt:en  
ENV LC_ALL pt_BR.UTF-8

# Seta variáveis de ambiente
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN chmod +x entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]

EXPOSE 5000

CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app" ]