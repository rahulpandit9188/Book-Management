function validate()
{
    var flag=true;
    var A1 = document.getElementById("A1")
    if(A1.value.length==0)
        flag=false
    return flag;
}
