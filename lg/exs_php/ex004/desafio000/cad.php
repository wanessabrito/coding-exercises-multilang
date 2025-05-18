<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio000</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <main>
            <h1>Resultado Final</h1>
        <?php 

            $numero = $_GET["numero"] ?? "0";

            $antecessor = $numero - 1;
            $sucessor = $numero + 1;

            //. ($num -1) .
    
            echo "O número escolhido foi <strong>$numero</strong><br>
            O seu antecessor é $antecessor<br>O seu sucessor é $sucessor";
            
              ?>

            <button onclick="javascript:history.go(-1)">⬅Voltar</button>

        </main>
</body>
</html>