import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { ApiService } from '../api.service';
import { Genre } from '../interfaces';
@Component({
  selector: 'app-addbook',
  templateUrl: './addbook.component.html',
  styleUrls: ['./addbook.component.css']
})
export class AddbookComponent implements OnInit{
  constructor(private api: ApiService){}
  name : string = ""
  author : string =""
  price : number = 0
  pic: string=""
  genre_id : number = 0
  genres : Genre[]= []

  form = new FormGroup({
    genreList: new FormControl('', Validators.required)
  });
  
  ngOnInit(): void {
    this.api.getGenres().subscribe((res)=>{
      this.genres = res 
    })
  }
  createBook(n: string, a: string, p: number, pic: string, g: number){
    this.api.addBookApi(n,a,p,pic,g)
  }
}
