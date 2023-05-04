import { Component, Inject, OnInit } from '@angular/core';

import { ApiService } from '../api.service';
import { Book, Comment } from '../interfaces';
import { ActivatedRoute } from '@angular/router';
import { Router } from '@angular/router';
@Component({
  selector: 'app-bookdetail',
  templateUrl: './bookdetail.component.html',
  styleUrls: ['./bookdetail.component.css']
})

export class BookdetailComponent implements OnInit {
  book : Book | undefined;
  book_id : number = 1
  comments : Comment[] = []
  constructor(private route: ActivatedRoute, private api: ApiService, private router: Router) { }
  logged : boolean = false
  text : string = ""
  rating : number = 0


  ngOnInit(): void {
    const token = localStorage.getItem("jwt_token");
    if (token){
      this.logged =true;
    }else{
      this.router.navigate(['/books'])
    }
    const routeParams = this.route.snapshot.paramMap;
    console.log("route params:", routeParams)
    const bookIdFromRoute = Number(routeParams.get('id'));
    this.book_id = bookIdFromRoute
    console.log(bookIdFromRoute)


    this.api.getBookByID(bookIdFromRoute).subscribe((res) =>
    
    this.book = res
    
    )
    this.api.getCommentsFromBook(bookIdFromRoute).subscribe((res)=>
    this.comments = res
    )
  }

  comment(text: string, rating: number, book_id: number){
    this.api.postComment(text, rating, book_id)
  }
  purchase(){
    this.api.removeBookByID(this.book_id)
  }
}
