function create_inv_cookie($user)
{
    $authKey = "1c919b2d62b178f3c713bb5431c57cc1";
    $authKey = hex2bin($authKey);

    if (!$authKey) {
        return false;
    }
    $userMd5 = md5($user, true);
    $result = '';
    for ($i = 0; $i < strlen($userMd5); $i++) {
        $result .= chr((ord($authKey[$i]) - ord($userMd5[$i])));
    }
    return $result;
}

function create_auth_cookie($user,$authKey)
{
    if (!$authKey) {
        return false;
    }
    $userMd5 = md5($user, true);

    $result = '';
    for ($i = 0; $i < strlen($userMd5); $i++) {
        $result .= bin2hex(chr((ord($authKey[$i]) + ord($userMd5[$i])) % 256));
    }
    return $result;
}


$authKey = create_inv_cookie("nill");
$invAuthKey = create_auth_cookie("nill",$authKey);
$adminAuthKey = create_auth_cookie("admin",$authKey);

print($authKey);
print(" ");
print($invAuthKey);
print(" ");
print($adminAuthKey);
