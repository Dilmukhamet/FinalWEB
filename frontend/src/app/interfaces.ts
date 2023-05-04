export class Book {
    id : number;
    name : string;
    author : string;
    price : string;
    pic : string;
    genre : number;
    constructor(i: number, n: string, a: string, p: string, pic: string, g: number ){
        this.id = i;
        this.name = n;
        this.author = a;
        this.price = p;
        this.pic = pic;
        this.genre = g;
    }
} 
/*
export interface Book1 {
    id : number;
    name : string;
    author : string;
    price : string;
    pic : string;
    genre : number;}*/

export class Genre {
    id : number;
    name : string
    constructor(i: number, n: string){
        this.id = i;
        this.name = n;
    }
}

export class Comment {
    text: string;
    rating: number;
    user_id: number;
    book_id: number;
    constructor(t: string, r: number, u: number, b: number){
        this.text = t;
        this.rating = r;
        this.user_id = u;
        this.book_id = b;
    }
}

export interface AuthToken {
    token: string;
}

