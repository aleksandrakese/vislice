% rebase('base.tpl')
% import model
<table>

  <tr>
    <td>
      <h3> ID igre je {{ id_igre }} </h3>
    </td>
  </tr>
    

  <tr>
    <td>
      <h3> {{ igra.pravilni_del_gesla() }} </h3>
    </td>
  </tr>

  <tr>
    <td><h3> Neuspeli poskusi </h3></td>
    <td>
      {{ igra.nepravilni_ugibi() }}
    </td>
  </tr>

  % if poskus == model.ZMAGA or poskus == model.PORAZ:
  <form action="/nova_igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

  % else:

  <tr>
    <form action="/igra/" method='post'>
      <input type="text" name="poskus">
      <input type="submit" value="Ugibaj">
    </form>
  </tr>

  % end

</table>