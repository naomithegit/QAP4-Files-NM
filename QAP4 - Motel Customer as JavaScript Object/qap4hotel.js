//author. naomi moores
//date. november 16, 2023



const MotelGuest = {
    firstname: "Cleopatra ",
    lastname: "O'Driscoll",
    birthyear: "0001",
    gender: "Female",
    pymtMethod: "Credit Card - VISA",
    phone: "709-699-8773",

    visit: {
      checkInDate: "2023-09-09",
      checkOutDate: "2023-10-10",
    },
    
    address: {
      street: "666 Tutankhamun Crescent",
      city: "Pyramid Town",
      province: "RAH",
      postalCode : "R1A1H1",
    },

    roompreferences : [ "egyptian cotton sheets", "milk bath", "pet friendly", "Cairo King mattress"],

    
    likes : ["cats", "big jewelry", "crowns"],
    dislikes : ["scarab beetles", "sand", "traitors"],
    

    getAge: function(){
      const today = new Date();
      return today.getFullYear() - this.birthyear;
    },

    getLengthOfStay: function () {
      const checkInDate = new Date(this.visit.checkInDate);
      const checkOutDate = new Date(this.visit.checkOutDate);
      const timeDifference = checkOutDate.getTime() - checkInDate.getTime();
      const daysDifference = timeDifference / (1000 * 3600 * 24);
      return daysDifference;
    },


    };


  const lengthOfStay = MotelGuest.getLengthOfStay();


  //console.log(`Length of stay: ${lengthOfStay} days`);
    //console.log(MotelGuest.visit.timeDifference)
     //console.log(calculateLengthOfStay(checkInDate, checkOutDate))
     //console.log(naomi)
     console.log(MotelGuest)
     console.log(MotelGuest.likes[1])
     console.log(MotelGuest.dislikes)
     console.log(MotelGuest.getAge("0001"))

     console.log(`Once in a land very very far away, there lived a beautiful woman named ${MotelGuest.firstname}. She loved ${MotelGuest.likes[1]} but absolutely hated ${MotelGuest.dislikes[2]}! One day, after years of political intrigue and war she decided to 'come home out of it'. At ${MotelGuest.getAge()} years of age, she really wasn't getting any younger, so without a second thought Miss ${MotelGuest.firstname}${MotelGuest.lastname} packed up her ${MotelGuest.likes[0]} and her ${MotelGuest.likes[2]} to set sail from a land of ${MotelGuest.dislikes[0]} and ${MotelGuest.dislikes[1]} to a one of rain, drizzle and fog.`)

     console.log(`An aside. There was weather and ${MotelGuest.firstname} got stranded in New York for ${lengthOfStay} days but it was all good cuz she stayed at a lovely little boutique motel in the Village. She also had time to check out the Temple of Dendur at the Metropolitan Museum. Talk about amateur hour. Yikes.`)
 

     