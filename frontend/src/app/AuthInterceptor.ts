import { Injectable } from '@angular/core'
import { HttpInterceptor, HttpEvent, HttpHandler, HttpRequest} from '@angular/common/http'
import { Observable } from 'rxjs';

@Injectable()
export class AuthInterceptor implements HttpInterceptor{
    //urlsToNotUse: Array<string>;
    constructor() {
      /*  this.urlsToNotUse= [
            'myController1/myAction1/.+',
            'myController1/myAction2/.+',
            'myController1/myAction3'
          ];*/
      
    }
    intercept(req: HttpRequest<any>, next: HttpHandler): Observable<HttpEvent<any>> {
        const token = localStorage.getItem('jwt_token');

        if (token){
            const newReq = req.clone({
                headers: req.headers.set('Authorization', `JWT ${token}`)
            })
            return next.handle(newReq)
        }
        return next.handle(req)
    }

}