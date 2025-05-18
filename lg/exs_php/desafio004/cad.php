<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio 004</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <main>
        <h1>Analisador de Número Real</h1>
        
        <?php 
        $numero = $_GET["numero"];
        $nInteiro = floor($numero);
        $nFracionado = $numero - $nInteiro;
        ?>

<ul>
    <li>A parte inteira é <?php echo $nInteiro;?></li>
    <li>A parte fracionária do número é <?php  echo $nFracionado;?></li>
</ul>

<button onclick="javascript:history.go(-1)">Voltar</button>

    </main>
</body>
</html>