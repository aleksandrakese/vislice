% import model

<!DOCTYPE html>
<html>
<head>
  <title>Vislice</title>
</head>

<body>

  <table>
    <tr>
      <td>
        {{ igra.pravilni_del_gesla() }}
      </td>
    </tr>

    <tr>
      <td><h3> Neuspeli poskusi </h3></td>
      <td>
        {{ igra.nepravilni_ugibi() }}
      </td>
    </tr>

    % if poskus == model.ZMAGA or poskus == model.PORAZ:
    <form action="/igra/" method="post">
      <button type="submit">Nova igra</button>
    </form>

    % else:

    <tr>
      <form action="/igra/{{id_igre}}" method='post'>
        <input type="text" name="poskus">
        <input type="submit" value="Ugibaj">
      </form>
    </tr>

    % end

  </table>

</body>

</html>