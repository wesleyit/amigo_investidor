=====
Usage
=====

Para subir a API em uma máquina com docker, execute:

.. code-block:: console

    $ docker run -d --name amigo_investidor -p 8080:8080 wesleyit/amigo_investidor:latest

Após este comando o container já deve entrar em execução.

Para acompanhar o log, digite:

.. code-block:: console

    $ docker logs amigo_investidor -f

Saia com <CTRL+C>.
