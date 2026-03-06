/*
Context
 Geekdemy provides a wide variety of online education programmes. Students can purchase them and enroll in these programmes. Geekdemy offers attractive discounts through their coupons so that students can spend less while purchasing these programmes.
 

Programmes
 There are 3 different categories of online programmes, and the cost is different for each category. A student can purchase any number of programmes at a time.
 

 CERTIFICATION - Rs.3000 
 DEGREE - Rs. 5000 
 DIPLOMA - Rs 2500 
Coupons
 The discount coupons offered by Geekdemy are based on different criteria. Only one discount coupon can be applied at a time.
 

 B4G1 - This coupon is applied automatically if 4 or more programmes are being purchased. The student gets one programme for free. The lowest priced programme is given for FREE.
 
 DEAL_G20 - This coupon can be applied if the purchased programmes value is Rs.10,000/- or above. It provides a 20% discount on the total programme cost. The coupon needs to be applied explicitly to get a discount.
 
 DEAL_G5 - This coupon can only be applied if there are a minimum of 2 programmes being purchased. It provides a 5% discount on the total programme cost. The coupon needs to be applied explicitly to get a discount.
 
Enrollment Fee
 If the total programme cost is below Rs. 6666/, an extra enrollment fee Rs.500/- is added to the cart. The enrollment fee is applied after the discount. If the total programme cost is or above Rs.6666/- the enrollment fee is waived off.
 

Pro Membership Fee
 A student can choose to purchase a Pro Membership for a small amount of Rs.200/- . The pro membership provides an additional membership discount on each of the individual programmes on top of the other discounts.
 

 DIPLOMA - 1% discount 
 CERTIFICATION - 2% discount 
 DEGREE - 3% discount
 

Goal
 Build a command-line application to purchase different kinds of programmes from Geekdemy. The application should generate a total bill of the programmes after applying the discounts, if any.

Assumptions
 A student can add any number of programmes to the cart. 
 A student can add the same category of programme multiple times. 
 A student can choose to buy pro membership or not.  
 If a student has  purchased a pro membership and has applied for a coupon, The coupon discount is applied after applying the pro membership discounts. 
 The B4G1 coupon gets auto applied when there are more than 4 programmes in the cart. 
 All the other coupons (DEAL_G20, DEAL_G5) need to be applied on the cart, if not no discount is provided. 
 If there are 4 or more programmes in the cart and the student has applied for a coupon other than B4G1, B4G1 coupon will be used, and the other coupon needs to be ignored. 
 If 2 or more coupons are applied, the higher value coupon needs to be considered (except in the case of 4 or more programmes; in that case B4G1 is auto applied).
	eg: if a student applies the coupon DEAL_G20 and DEAL_G5 and the purchase value is greater than 10,000, then DEAL_G20 needs to be considered.
	eg: if a student applies the coupon DEAL_G20 and DEAL_G5 and the purchase value is greater than 10,000, then DEAL_G20 needs to be considered. 

Input Commands & Format
 Your program should take the purchase details as input.
 

ADD_PROGRAMME <CATEGORY_1> <QUANTITY> 

 Adds the specified category and quantity of programme to the purchases 
APPLY_COUPON <COUPON_NAME> 

 Applies the discount coupon to the total value of the purchases 
ADD_PRO_MEMBERSHIP 

 Adds a pro membership along with other purchases. It applies a membership discount on each programme. 
PRINT_BILL 

 Prints the programme purchase details. 
Output Commands & Format
 Your program should print the bill details.
 

SUB_TOTAL <AMOUNT> 

 This includes all the items purchased (programmes and pro membership) 
 Print the cost of all the programmes purchased, after applying a pro membership discount (if applicable). 
COUPON_DISCOUNT <COUPON_NAME> <AMOUNT> 

 Print the applied coupon and the discounted amount 
 If the coupon is not applicable, Print “DISCOUNT NONE 0 
TOTAL_PRO_DISCOUNT <AMOUNT> 

 Print the total amount discounted through pro membership. 
PRO_MEMBERSHIP_FEE <AMOUNT> 

 Print the pro membership fee. 
ENROLLMENT_FEE <AMOUNT> 

 Print the enrollment fee. 
TOTAL <AMOUNT> 

 Print the total value of the shopping cart after discount is applied. 
Sample Input/Output 1
INPUT	OUTPUT
ADD_PROGRAMME CERTIFICATION 1
ADD_PROGRAMME DEGREE 1 
ADD_PROGRAMME DIPLOMA 2
APPLY_COUPON DEAL_G20
PRINT_BILL	SUB_TOTAL 13000.00
COUPON_DISCOUNT B4G1 2500.00
TOTAL_PRO_DISCOUNT 0.00
PRO_MEMBERSHIP_FEE 0.00
ENROLLMENT_FEE 0.00
TOTAL 10500.00

Sample Input/Output 2
INPUT	OUTPUT
ADD_PROGRAMME DEGREE 1 
ADD_PROGRAMME DIPLOMA 2
APPLY_COUPON DEAL_G20
APPLY_COUPON DEAL_G5
PRINT_BILL	SUB_TOTAL 10000.00
COUPON_DISCOUNT DEAL_G20 2000.00
TOTAL_PRO_DISCOUNT 0.00
PRO_MEMBERSHIP_FEE 0.00
ENROLLMENT_FEE 0.00
TOTAL 8000.00


*/

const fs = require("fs");

// ==================== DOMAIN MODELS ====================

class Programme {
    constructor(type, price) {
        this.type = type;
        this.price = price;
    }

    getType() {
        return this.type;
    }

    getPrice() {
        return this.price;
    }

    getProMembershipDiscount() {
        const discounts = {
            DIPLOMA: 0.01,
            CERTIFICATION: 0.02,
            DEGREE: 0.03
        };
        return discounts[this.type] || 0;
    }
}

class Cart {
    constructor() {
        this.programmes = [];
        this.appliedCoupons = [];
        this.hasProMembership = false;
    }

    addProgramme(programme, quantity) {
        for (let i = 0; i < quantity; i++) {
            this.programmes.push(programme);
        }
    }

    applyCoupon(couponName) {
        this.appliedCoupons.push(couponName);
    }

    addProMembership() {
        this.hasProMembership = true;
    }

    getProgrammes() {
        return this.programmes;
    }

    getAppliedCoupons() {
        return this.appliedCoupons;
    }

    hasProMembershipEnabled() {
        return this.hasProMembership;
    }

    getTotalProgrammes() {
        return this.programmes.length;
    }
}

class Bill {
    constructor() {
        this.subTotal = 0;
        this.couponDiscount = 0;
        this.appliedCouponName = "NONE";
        this.totalProDiscount = 0;
        this.proMembershipFee = 0;
        this.enrollmentFee = 0;
        this.total = 0;
    }

    print() {
        console.log(`SUB_TOTAL ${this.subTotal.toFixed(2)}`);
        console.log(`COUPON_DISCOUNT ${this.appliedCouponName} ${this.couponDiscount.toFixed(2)}`);
        console.log(`TOTAL_PRO_DISCOUNT ${this.totalProDiscount.toFixed(2)}`);
        console.log(`PRO_MEMBERSHIP_FEE ${this.proMembershipFee.toFixed(2)}`);
        console.log(`ENROLLMENT_FEE ${this.enrollmentFee.toFixed(2)}`);
        console.log(`TOTAL ${this.total.toFixed(2)}`);
    }
}

// ==================== STRATEGY PATTERN (DISCOUNT STRATEGIES) ====================

class DiscountStrategy {
    canApply(cart, subtotal) {
        return false;
    }

    calculateDiscount(cart, subtotal) {
        return 0;
    }

    getName() {
        return "";
    }
}

class B4G1Strategy extends DiscountStrategy {
    canApply(cart) {
        return cart.getTotalProgrammes() >= 4;
    }

    calculateDiscount(cart) {
        if (!this.canApply(cart)) return 0;
        
        // Find the lowest priced programme
        const prices = cart.getProgrammes().map(p => p.getPrice());
        return Math.min(...prices);
    }

    getName() {
        return "B4G1";
    }
}

class DealG20Strategy extends DiscountStrategy {
    canApply(cart, subtotal) {
        return subtotal >= 10000;
    }

    calculateDiscount(cart, subtotal) {
        if (!this.canApply(cart, subtotal)) return 0;
        return subtotal * 0.20;
    }

    getName() {
        return "DEAL_G20";
    }
}

class DealG5Strategy extends DiscountStrategy {
    canApply(cart) {
        return cart.getTotalProgrammes() >= 2;
    }

    calculateDiscount(cart, subtotal) {
        if (!this.canApply(cart)) return 0;
        return subtotal * 0.05;
    }

    getName() {
        return "DEAL_G5";
    }
}

// ==================== DISCOUNT MANAGER ====================

class DiscountManager {
    constructor() {
        this.strategies = {
            B4G1: new B4G1Strategy(),
            DEAL_G20: new DealG20Strategy(),
            DEAL_G5: new DealG5Strategy()
        };
    }

    getBestDiscount(cart, subtotal) {
        // Rule: If 4+ programmes, B4G1 is auto-applied and others are ignored
        if (cart.getTotalProgrammes() >= 4) {
            const b4g1 = this.strategies.B4G1;
            return {
                name: b4g1.getName(),
                amount: b4g1.calculateDiscount(cart, subtotal)
            };
        }

        // Evaluate all applied coupons and select the one with maximum discount
        let maxDiscount = 0;
        let bestCoupon = "NONE";

        for (const couponName of cart.getAppliedCoupons()) {
            const strategy = this.strategies[couponName];
            if (strategy && strategy.canApply(cart, subtotal)) {
                const discount = strategy.calculateDiscount(cart, subtotal);
                if (discount > maxDiscount) {
                    maxDiscount = discount;
                    bestCoupon = couponName;
                }
            }
        }

        return {
            name: bestCoupon,
            amount: maxDiscount
        };
    }
}

// ==================== FACTORY PATTERN ====================

class ProgrammeFactory {
    constructor() {
        this.catalogue = {
            CERTIFICATION: { type: "CERTIFICATION", price: 3000 },
            DEGREE: { type: "DEGREE", price: 5000 },
            DIPLOMA: { type: "DIPLOMA", price: 2500 }
        };
    }

    createProgramme(type) {
        const config = this.catalogue[type];
        if (!config) {
            throw new Error(`Programme type ${type} not found`);
        }
        return new Programme(config.type, config.price);
    }
}

// ==================== BILL CALCULATOR (CHAIN OF RESPONSIBILITY) ====================

class BillCalculator {
    constructor(discountManager) {
        this.discountManager = discountManager;
    }

    calculate(cart) {
        const bill = new Bill();

        // Step 1: Calculate raw subtotal
        let rawTotal = 0;
        for (const programme of cart.getProgrammes()) {
            rawTotal += programme.getPrice();
        }

        // Step 2: Apply pro membership discounts
        let proDiscount = 0;
        if (cart.hasProMembershipEnabled()) {
            for (const programme of cart.getProgrammes()) {
                proDiscount += programme.getPrice() * programme.getProMembershipDiscount();
            }
        }

        const subtotalAfterProDiscount = rawTotal - proDiscount;
        bill.subTotal = subtotalAfterProDiscount;
        bill.totalProDiscount = proDiscount;

        // Step 3: Apply best coupon discount
        const bestDiscount = this.discountManager.getBestDiscount(cart, subtotalAfterProDiscount);
        bill.couponDiscount = bestDiscount.amount;
        bill.appliedCouponName = bestDiscount.name;

        // Step 4: Calculate total after coupon discount
        let totalAfterDiscounts = subtotalAfterProDiscount - bill.couponDiscount;

        // Step 5: Add pro membership fee if applicable
        if (cart.hasProMembershipEnabled()) {
            bill.proMembershipFee = 200;
        }

        // Step 6: Calculate enrollment fee
        if (totalAfterDiscounts < 6666) {
            bill.enrollmentFee = 500;
        }

        // Step 7: Calculate final total
        bill.total = totalAfterDiscounts + bill.proMembershipFee + bill.enrollmentFee;

        return bill;
    }
}

// ==================== COMMAND PATTERN ====================

class Command {
    execute(args) {
        throw new Error("Execute method must be implemented");
    }
}

class AddProgrammeCommand extends Command {
    constructor(cart, programmeFactory) {
        super();
        this.cart = cart;
        this.programmeFactory = programmeFactory;
    }

    execute(args) {
        const [type, quantity] = args;
        const programme = this.programmeFactory.createProgramme(type);
        this.cart.addProgramme(programme, parseInt(quantity));
    }
}

class ApplyCouponCommand extends Command {
    constructor(cart) {
        super();
        this.cart = cart;
    }

    execute(args) {
        const [couponName] = args;
        this.cart.applyCoupon(couponName);
    }
}

class AddProMembershipCommand extends Command {
    constructor(cart) {
        super();
        this.cart = cart;
    }

    execute(args) {
        this.cart.addProMembership();
    }
}

class PrintBillCommand extends Command {
    constructor(cart, billCalculator) {
        super();
        this.cart = cart;
        this.billCalculator = billCalculator;
    }

    execute(args) {
        const bill = this.billCalculator.calculate(this.cart);
        bill.print();
    }
}

// ==================== COMMAND INVOKER ====================

class CommandInvoker {
    constructor() {
        this.commandMap = new Map();
    }

    register(commandName, command) {
        this.commandMap.set(commandName, command);
    }

    execute(commandName, args) {
        const command = this.commandMap.get(commandName);
        if (!command) {
            throw new Error(`Command ${commandName} not found`);
        }
        command.execute(args);
    }
}

// ==================== MAIN APPLICATION ====================

const filename = process.argv[2];

fs.readFile(filename, "utf8", (err, data) => {
    if (err) throw err;

    // Initialize dependencies
    const cart = new Cart();
    const programmeFactory = new ProgrammeFactory();
    const discountManager = new DiscountManager();
    const billCalculator = new BillCalculator(discountManager);

    // Setup command invoker
    const commandInvoker = new CommandInvoker();
    commandInvoker.register("ADD_PROGRAMME", new AddProgrammeCommand(cart, programmeFactory));
    commandInvoker.register("APPLY_COUPON", new ApplyCouponCommand(cart));
    commandInvoker.register("ADD_PRO_MEMBERSHIP", new AddProMembershipCommand(cart));
    commandInvoker.register("PRINT_BILL", new PrintBillCommand(cart, billCalculator));

    // Process input commands
    const inputLines = data.toString().trim().split("\n");
    for (const line of inputLines) {
        const parts = line.trim().split(" ");
        const commandName = parts[0];
        const args = parts.slice(1);
        
        commandInvoker.execute(commandName, args);
    }
});
