<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Desafio002</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <main>
        <h1>Conversor de Moedas v1.0</h1>
        <?php 
        $numero = $_GET["numero"] ?? "0";

        $conversor = $numero/5.47;

        echo "Seus R$ " . number_format($numero, 2, ',', '.') . " equivalem a <strong>US$ " . number_format($conversor, 2, '.', ',') . "</strong> <br><br> <strong>*Cotação fixa de R$ 5,47</strong> informada diretamente no código<br><br>";

        
        ?>
        <button onclick="javascript:history.go(-1)">Voltar</button>
    </main>
</body>
</html>