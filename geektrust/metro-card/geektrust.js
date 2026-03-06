const fs = require("fs")

const filename = process.argv[2]

/*Context
 A new metro train has been launched from the Central station to the Airport. It is a non-stop train, which means the train will stop only at the Airport with no intermediate stops. 
It is also possible to return from the Airport back to the Central station. This is also a non-stop journey.
 

MetroCard
 Metro authority prefers money to be collected via MetroCard. MetroCard is an electronic payment utility that can be used to pay for the metro travel charges. The MetroCard is like a wallet loaded with money. Each person traveling in this metro must carry a MetroCard and each card will have a unique number. 
 

 To travel by this train, one needs a MetroCard. If the MetroCard doesn’t have sufficient balance, then the remaining cost for the travel needs to be paid by recharging the MetroCard. This auto recharge loads only the required amount of money for the journey and the station collects a 2% service fee for the transaction. 

Travel charges
 Costs for the journey are based on the passenger's age. It is categorized as below
 


Journey Types
 Travel charges are different for a single trip and for a return journey. When a passenger takes a return journey, there is a discount of 50% for the travel charges of the return journey. 
 

 For eg: If a senior citizen travels from Central to Airport, the travel charge collected is 100. If the same citizen travels back to Central station,  the amount collected for the return journey is 50. If the same citizen passes a third time on the same day, it will be treated as a new single journey and the travel charge collected is 100.
 

Goal
 Your task is to build a solution that calculates various travel charges collected at each station and print the collection summary and passenger summary. 
 

 The collection summary should give a breakup of the total amount collected and the total discount given. 
 The passenger summary should display the total number of passengers traveled per type in descending order of the passenger count. 
 If any of the passenger type have same value for passenger count then display in the ascending order of the passenger type for that case. 
	Ex:If ADULT and KID has same value then display it as 
	ADULT <no_of_passengers>
	KID <no_of_passengers>
 
Assumptions
 All passengers should have a MetroCard. 
 If a passenger does not have sufficient balance in the MetroCard, then the MetroCard needs to be recharged before taking up the journey. 
 The service fee for doing the recharge is collected by the origin station of the journey. 
 The passenger count is calculated based on journeys eg: if the same passenger travels twice, the count is 2.
 
*/

/*
ADULT = 200
SENIOR_CITIZEN = 100
KID = 50
*/

class Card {
    constructor(cardId, balance) {
        this.cardId = cardId;
        this.balance = balance;
        this.singleTripStatus = false;
    }

    getTripFare(passengerType) {
        const fareMap = {
            ADULT: 200,
            SENIOR_CITIZEN: 100,
            KID: 50,
        }

        let discount = 0;
        let totalFare = 0;

        totalFare = this.singleTripStatus ? fareMap[passengerType] : fareMap[passengerType] / 2;
        discount = this.singleTripStatus ? 0 : fareMap[passengerType] / 2;
        return [totalFare, discount];
    }

    setWalletBalance(amount) {
        const tax = 0.02;
        let totalFare = 0;
        let updatedBalance = this.balance - amount;

        if(updatedBalance < 0) {
            totalFare += - tax * updatedBalance;
            updatedBalance = 0;
        }
        this.balance = updatedBalance;
        this.singleTripStatus = !this.singleTripStatus;
        return totalFare;
    }
}

class Station {
    constructor(stationName) {
        this.stationName = stationName;
        this.totalSale = 0;
        this.totalDiscount = 0;
        this.passengerCount = {
            ADULT: 0,
            SENIOR_CITIZEN: 0,
            KID: 0,
        }
    }

    getStationSummary() {
        console.log(`TOTAL_COLLECTION ${this.stationName} ${this.totalSale} ${this.totalDiscount}`);
        console.log(`PASSENGER_TYPE_SUMMARY`);
        const sortedPassengerCount = Object.entries(this.passengerCount).sort((a, b) => b[1] - a[1]);
        for(let [passengerType, count] of sortedPassengerCount) {
            console.log(`${passengerType} ${count}`);
        }
    }

    updateTravellerEntry(passengerType, fare, discount) {
        this.passengerCount[passengerType]++;
        this.totalSale += fare;
        this.totalDiscount += discount;
    }

}

fs.readFile(filename, "utf8", (err, data) => {
    if (err) throw err
    var inputLines = data.toString().split("\n")
    const stations = {'CENTRAL': new Station('CENTRAL'), 'AIRPORT': new Station('AIRPORT')};
    const cards = {};

    // Add your code here to process input commands
    for(let line of inputLines) {
        let [command, ...args] = line.replace("\r", "").split(" ");
        switch(command) {
            case 'BALANCE': {
                const [cardId, amount] = args
                if(!cards[cardId]) {
                    cards[cardId] = new Card(cardId, amount);
                } else {
                    cards[cardId].setWalletBalance(amount);
                }
                break;
            }
            case 'CHECK_IN': {
                const [cardId, passengerType, stationName] = args;
                if(!cards[cardId]) {
                    console.log(`INVALID_CARD ${cardId}`);
                    continue;
                }
                const [fare, discount] = cards[cardId].getTripFare(passengerType);
                cards[cardId].setWalletBalance(fare);
                stations[stationName].updateTravellerEntry(passengerType, fare, discount);
                break;
            }
            case 'PRINT_SUMMARY': {
                for(const [stationName, station] of Object.entries(stations)) {
                    station.getStationSummary();
                }
                break;
            }
            default: {
                console.log(`INVALID_COMMAND ${command}`);
            }
        }
    }
})

