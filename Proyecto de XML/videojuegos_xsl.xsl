<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" encoding="UTF-8"/>
    <xsl:template match="/">
        <html>
            <head>
                <title>Lista de Videojuegos</title>
                <style>
                    table { border-collapse: collapse; width: 100%; }
                    th, td { border: 1px solid black; padding: 8px; text-align: left; }
                    th { background-color: #f2f2f2; }
                </style>
            </head>
            <body>
                <h1>Lista de Videojuegos</h1>
                <table>
                    <tr>
                        <th>ID</th>
                        <th>Título</th>
                        <th>Desarrollador</th>
                        <th>Plataforma</th>
                        <th>Género</th>
                        <th>Lanzamiento</th>
                    </tr>
                    <xsl:for-each select="videojuegos/videojuego">
                        <tr>
                            <td><xsl:value-of select="@id"/></td>
                            <td><xsl:value-of select="titulo"/></td>
                            <td><xsl:value-of select="desarrollador"/></td>
                            <td><xsl:value-of select="plataforma"/></td>
                            <td><xsl:value-of select="genero"/></td>
                            <td><xsl:value-of select="lanzamiento"/></td>
                        </tr>
                    </xsl:for-each>
                </table>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>