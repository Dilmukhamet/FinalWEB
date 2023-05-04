import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { Book } from '../interfaces';
import { Router } from '@angular/router';
@Component({
  selector: 'app-books',
  templateUrl: './books.component.html',
  styleUrls: ['./books.component.css']
})
export class BooksComponent implements OnInit{
  books : Book[] = []
  logged: boolean = false;
  mail: string = "";
  password: string = "";
  constructor(private api: ApiService, private router: Router){}

  ngOnInit(): void {
    console = console 
    const token = localStorage.getItem("jwt_token");
    if (token){
      this.logged =true;
    }
    this.api.getBoooks().subscribe((res) =>
    this.books = res
    )
    console.log(this.books)
  }

  auth(){
    //this.api.login1(this.mail, this.password),subscribe()
    this.api.login1(this.mail, this.password).subscribe((res)=>{
      //console.log(res)
      localStorage.setItem('jwt_token', res.token)
    })
    const token = localStorage.getItem("jwt_token");
    if(token){
    this.logged = true
    }
    
  }
  exit(){
    this.api.logout()
    this.logged = false
  }
  createBook(){
    this.router.navigate(['createbook'])
  }
}
