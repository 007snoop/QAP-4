class Customer {
    constructor(name, birthDate, gender, roomPreferences, paymentMethod, mailingAddress, phoneNumber, checkInDate, checkOutDate) {
      this.name = name;
      this.birthDate = new Date(birthDate);
      this.gender = gender;
      this.roomPreferences = roomPreferences;
      this.paymentMethod = paymentMethod;
      this.mailingAddress = mailingAddress; // Object with address details
      this.phoneNumber = phoneNumber;
      this.checkInDate = new Date(checkInDate);
      this.checkOutDate = new Date(checkOutDate);
    }
  
    getAge(age) {
      const today = new Date();
      let age = today.getFullYear() - this.birthDate.getFullYear();
      const monthDiff = today.getMonth() - this.birthDate.getMonth();
      if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < this.birthDate.getDate())) {
        age--;
      }
      return age;
    }
  
    getStayDuration() {
      const duration = this.checkOutDate - this.checkInDate;
      const days = Math.ceil(duration / (1000 * 60 * 60 * 24)); // Convert milliseconds to days
      return days;
    }
  
    getDescription() {
      return `
        Customer Name: ${this.name}<br>
        Gender: ${this.gender}<br>
        Age: ${this.getAge()}<br>
        Phone Number: ${this.phoneNumber}<br>
        Payment Method: ${this.paymentMethod}<br>
        Mailing Address: ${this.mailingAddress.street}, ${this.mailingAddress.city}, ${this.mailingAddress.state}, ${this.mailingAddress.zip}<br>
        Room Preferences: ${this.roomPreferences.join(', ')}<br>
        Check-In Date: ${this.checkInDate.toDateString()}<br>
        Check-Out Date: ${this.checkOutDate.toDateString()}<br>
        Duration of Stay: ${this.getStayDuration()} days
      `;
    }
  }
  
  function handleFormSubmit(event) {
    event.preventDefault();
  
    const name = document.getElementById('name').value;
    const birthDate = document.getElementById('birthDate').value;
    const gender = document.getElementById('gender').value;
    const roomPreferences = document.getElementById('roomPreferences').value.split(',').map(pref => pref.trim());
    const paymentMethod = document.getElementById('paymentMethod').value;
    const mailingAddress = document.getElementById('mailingAddress').value.split(',');
    const phoneNumber = document.getElementById('phoneNumber').value;
    const checkInDate = document.getElementById('checkInDate').value;
    const checkOutDate = document.getElementById('checkOutDate').value;
  
    const mailingAddressObj = {
      street: mailingAddress[0].trim(),
      city: mailingAddress[1].trim(),
      province: mailingAddress[2].trim(),
      postalCode: mailingAddress[3].trim()
    };
  
    // customer object
    const customer = new Customer(
      name,
      birthDate,
      gender,
      roomPreferences,
      paymentMethod,
      mailingAddressObj,
      phoneNumber,
      checkInDate,
      checkOutDate
    );
  
    // display customer information
    document.getElementById('customer-info').innerHTML = customer.getDescription();
  }
  
  // Attach the form submit handler
  document.getElementById('customer-form').addEventListener('submit', handleFormSubmit);