
  function run(sol){
  if (sol['*'] == 0.0)
  {
    swal({
      title:'Error!',
      text:'The given system of equation are not solvable',
      icon:'error'
    })
    return;
  }
  const content = document.createElement('div')
  const list = document.createElement('ul')
  for(const item in sol)
  {
    const e = document.createElement('li')
    e.innerHTML=`<b>${item}</b> = ${sol[item].toFixed(4)}`
    console.log(e)
    list.appendChild(e)
  }
  content.appendChild(list)
  content.style = "text-align:left;"
  console.log(content)
  swal({
    // html:true,
    title:"Solution",
    icon:"success",
    content
  });
}
