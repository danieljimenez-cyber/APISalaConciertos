FROM httpd:latest

# Copiar el archivo de configuración personalizado
COPY config/demo.apache.conf /usr/local/apache2/conf/httpd.conf

# Asegurar que el módulo alias está activado
RUN echo "LoadModule alias_module modules/mod_alias.so" > /usr/local/apache2/conf/extra/mod_alias.conf

# Incluir el archivo extra en la configuración de Apache
RUN echo "Include conf/extra/mod_alias.conf" >> /usr/local/apache2/conf/httpd.conf