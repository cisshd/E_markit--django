let deleteitem=(id)=>
{
    Swal.fire({
        title: 'هل أنت متأكد؟',
        text: "لن تتمكن من استرجاع هذا العنصر بعد الحذف!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'نعم، احذف!',
        cancelButtonText: 'إلغاء'
    }).then((result)=>{

        if(result.isConfirmed)
        {
           $.ajax({
             url: 'delete/' + id,
             type:'GET',
             
             success: function(result)
             {
                window.location.href='/'
             }

           });
        }

    



    });
   
}