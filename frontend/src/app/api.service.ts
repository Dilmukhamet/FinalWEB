import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, tap, throwError } from 'rxjs';
import { AuthToken } from './interfaces';


@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private http: HttpClient ) { }
  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type': 'application/json'
    })
  };

  login(mail: string, pass: string): Observable<any>{
    console.log("Auth Invoked")
    return this.http.post(
      "http://localhost:8000/auth",
      {
        email: mail,
        password: pass
      }
    ).pipe(tap(this.setToken))
  }

  login1(email: string, password: string): Observable<AuthToken>{
    return this.http.post<AuthToken>(
      "http://localhost:8000/auth",
      {
        email, 
        password
      }
    )
  }

  private setToken(response: any){
    if(response){
      localStorage.setItem("jwt_token", response.token)
    }else {
      localStorage.clear()
    }
  }

  postComment(text: string, rating: number, book_id: number){
    return this.http.post("http://localhost:8000/api/books/comments",
    {
      text,
      rating,
      book_id
    })
  }

  addBookApi(name: string, author: string, price: number, pic: string, genre_id: number) {
    return this.http.post("http://localhost:8000/api/books",
    {  
        name,
        author,
        price,
        pic,
        genre_id
    }
    )
  }

  getToken(){
    return localStorage.getItem('jwt_token')
  }
  logout(){
    this.setToken(null)
  }

  getBoooks(): Observable<any>{
    return this.http.get("http://localhost:8000/api/books/all")
  } 
  getBookByID(id: number): Observable<any>{
    return this.http.get("http://localhost:8000/api/books/" + id)
  }
  removeBookByID(id: number): Observable<any>{
    return this.http.delete("http://localhost:8000/api/books/" + id)
  }

  getGenres(): Observable<any>{
    return this.http.get("http://localhost:8000/api/books/all")
  } 
  getBooksByGenre(id: number): Observable<any>{
    return this.http.get("http://localhost:8000/api/books/genres/" + id )
  } 
  getCommentsFromBook(id: number): Observable<any>{
    return this.http.get("http://localhost:8000/api/books/comments/" + id )
  }


}
