// console.log("我学会JS引入了")
// const a = "zhanghao"
// const b = "男"
// const c = 175
// console.log(a,b,c)
// let name
// console.log(typeof name)
// console.log(typeof a)
// console.log(typeof c)
// console.log(typeof null)

// let last_year = "2000"
// let next_year = "2026"
// let year = parseInt(next_year) - parseInt(last_year)
// console.log(year)

// let num = 10
// if (num % 2 === 0){
//     console.log("奇数")
// }
// else{
//     console.log("偶数")
// }
// let x = 3
// switch(x){
//     case 1:
//     console.log("星期一")
//     break
//     case 2:
//     console.log("星期二")
//     break
//     case 3:
//     console.log("星期三")
//     break
//     case 4:
//     console.log("星期四")
//     break
//     case 5:
//     console.log("星期五")
//     break
//     case 6:
//     console.log("星期六")
//     break
//     case 7:
//     console.log("星期日")
//     break
// }

// let num = 10
// if(num >= 0 && num < 10){
//     console.log("天气太冷应该穿羽绒服")
// }
// else if(num >= 10 && num <= 20){
//     console.log("天气稍冷建议穿薄外套")
// }
// else if(num >= 20 && num <= 30){
//     console.log("天气炎热应该穿短袖")
// }
// else if(num >= 30 && num <= 40){
//     console.log("天气太热，应该不出门")
// }

// let x = 3
// switch(x){
//     case 1:
//     console.log("一月")
//     break
//     case 2:
//     console.log("二")
//     break
//     case 3:
//     console.log("三")
//     break
//     case 4:
//     console.log("四")
//     break
//     case 5:
//     console.log("五")
//     break
//     case 6:
//     console.log("六")
//     break
//     case 7:
//     console.log("日")
//     break
//     case 8:
//     console.log("星期日")
//     break
//     case 9:
//     console.log("星期日")
//     break
//     case 10:
//     console.log("星期日")
//     break
//     case 11:
//     console.log("星期日")
//     break
//     case 12:
//     console.log("星期日")
//     break
// }



// for(i = 10;i > 0;i--){
//     console.log(i)
// }

// var a = 0
// for(i = 0;i < 101; i++){
//     a = a + i
// }
// console.log(a)

// while(i <= 20){
//     if(i % 2 === 0){
//         console.log(i)
//     }
// }

// for(i = 1; i <= 9; i++){
//     for(j = 1;j <= i; j++){
//         process.stdout.write(String(j) + "*" + String(i) + "=" + String(i * j) + " ")
//     }
//     process.stdout.write("\n")
// }


// function text(){
//     console.log("我学会函数了")
// }
// for(i = 0; i <= 10; i++){
//     text()
// }

// function asd(a,b){
//     if(a > b){
//         console.log(a)
//     }
//     else if(b > a){
//         console.log(b)
//     }
// }
// asd(5,9)

const abs = (a) => (a > 0 ? a : a * -1)
console.log(abs(-4))