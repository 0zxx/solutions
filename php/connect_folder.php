<?php
session_start();

if (isset($_POST['username']) && isset($_POST['password'])) {
    $htpasswd_file = '/caminho/para/arquivo/.htpasswd';
    $htpasswd_users = array();
    $lines = file($htpasswd_file, FILE_IGNORE_NEW_LINES | FILE_SKIP_EMPTY_LINES);

    foreach ($lines as $line) {
        list($user, $hash) = explode(':', $line);
        $htpasswd_users[$user] = $hash;
    }

    $username = $_POST['username'];
    $password = $_POST['password'];

    if (isset($htpasswd_users[$username])) {
        $hash = $htpasswd_users[$username];

        if (password_verify($password, $hash)) {
            $_SESSION['username'] = $username;
            header('Location: /caminho/para/pasta/protegida/');
            exit;
        }
    }

    $error = 'Usuário ou senha inválidos.';
}
?>
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <?php if (isset($error)): ?>
        <p><?php echo $error; ?></p>
    <?php endif; ?>

    <form method="post">
        <label for="username">Usuário:</label>
        <input type="text" name="username" id="username"><br>

        <label for="password">Senha:</label>
        <input type="password" name="password" id="password"><br>

        <input type="submit" value="Entrar">
    </form>
</body>
</html>
