myObj = {"People":
    [
        {
            "Id": 1,
            "FirstName": "Vu",
            "LastName": "Tran",
            "Active" : true
        },
        {
            "Id": 2,
            "FirstName": "Tran",
            "LastName": "Vu",
            "Active" : false
        }
    ]
}

console.log(typeof myObj.People[1].FirstName);
