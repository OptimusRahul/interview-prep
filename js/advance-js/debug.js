function calculateTotal(items) {
    let total = 0;
  
    for (let i = 0; i <= items.length; i++) {  // ❌ Bug here
      total += items[i].price;
    }
  
    return total;
  }
  
  const items = [
    { price: 10 },
    { price: 20 },
    { price: 30 }
  ];
  
  console.log("Total:", calculateTotal(items));