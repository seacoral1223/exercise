console.log("Hello, World!");

// var a = 10;//全局变量
// let b = 20;//局部变量
// const c = 30;//常量

// + - * / % #算术运算符
// == === != !== > < >= <= #比较运算符
// && || ! #逻辑运算符
// = += -= *= /= %= #赋值运算符

let flag = 0;
for (let i = 1; i < 100; i ++) {
	for (j = 2; j < i; j ++) {
		if (i % j === 0) {
			flag = 0
			break
		} else {
			flag = 1
		}
	}
	if (flag === 1) {
		console.log(i)
	}
}


document.write("这是一个标题");